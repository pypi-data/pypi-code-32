import threading
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from easygraphics.image import Image


class GraphWin(QWidget):
    """
    Main Window for painting graphics


    we use an Image object (self._canvas) to save the painted contents

    how to process repaint event:
    if we are in immediate mode (RENDER_AUTO, self._immediate=True) ,
        we directly paint the saved contents to the window
    if we are in manual refresh mode (RENDER_MANUAL, self._immediate=False),
        we use another image object( self._device_image) as an intermediary
        the contents on this object is painted to the window
        and this object is synced with self._screen manually
    """

    def __init__(self, width, height, app: QApplication):
        super().__init__();
        self._width = width;
        self._height = height;
        self._wait_event = threading.Event()
        self._mouse_event = threading.Event()
        self._key_event = threading.Event()
        self._char_key_event = threading.Event()
        self._key_msg = _KeyMsg()
        self._key_char_msg = _KeyCharMsg()
        self._mouse_msg = _MouseMsg()
        self.setGeometry(100, 100, width, height)
        self._init_screen(width, height)
        self._is_run = True
        self._immediate = True
        self._last_update_time = time.time_ns()
        self._skip_count = 0
        self._app = app

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def _init_screen(self, width, height):
        screen_image = QImage(width, height, QImage.Format_ARGB32_Premultiplied)
        p = QPainter()
        p.begin(screen_image)
        p.fillRect(0, 0, width, height, Qt.white)
        p.end()
        self._canvas = Image(screen_image)
        self._device_image = screen_image.copy()
        self.real_update()

    def get_canvas(self):
        return self._canvas;

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        if self._immediate:
            p.drawImage(0, 0, self._canvas.get_image())
        else:
            p.drawImage(0, 0, self._device_image)
        p.end()

    def invalid(self):
        """
        try to invalidate window

        if is in immediate mode (MODE_AUTO), the window is updated and repaint;
        otherwise, the window is not updated
        """
        if self._immediate:
            self.update()

    def set_immediate(self, immediate: bool):
        self._immediate = immediate

    def is_immediate(self) -> bool:
        return self._immediate

    def mousePressEvent(self, e: QMouseEvent):
        self._wait_event.set()
        self._mouse_msg.set_event(e)
        self._mouse_event.set()

    def mouseMoveEvent(self, e: QMouseEvent):
        self._mouse_msg.set_event(e)
        self._mouse_event.set()

    def keyPressEvent(self, e: QKeyEvent):
        self._wait_event.set()
        if e.key() < 127:
            # ascii char key pressed
            self._key_char_msg.set_char(e)
            self._char_key_event.set()
        self._key_msg.set_event(e)
        self._key_event.set()

    def pause(self):
        self._wait_event.clear()
        self._wait_event.wait()

    def closeEvent(self, QCloseEvent):
        self._is_run = False
        self._wait_event.set()
        self._mouse_event.set()
        self._key_event.set()
        self._char_key_event.set()
        self._app.quit()

    def is_run(self) -> bool:
        return self._is_run

    def real_update(self):
        """
        really update and repaint the window

        the intermediary image (self._device_image) is synced with the canvas
        """
        painter = QPainter()
        painter.begin(self._device_image)
        painter.drawImage(0, 0, self._canvas.get_image().copy())
        painter.end()
        self.update()
        self._last_update_time = time.time_ns()

    def delay(self, ms):
        """
        delay ms milliseconds
        :param ms: time to delay (in milliseconds)
        """
        nanotime = ms * 1000000
        start_wait_time = time.time_ns()
        self.real_update()
        while time.time_ns() - start_wait_time < nanotime:
            time.time_ns()

    def delay_fps(self, fps):
        """
        delay to control fps without frame skiping

        never skip frames
        """
        nanotime = 1000000000 // fps
        if self._last_update_time == 0:
            self._last_update_time = time.time_ns()
        while time.time_ns() - self._last_update_time < nanotime:
            time.time_ns()
        self.real_update()

    def delay_jfps(self, fps, max_skip_count=10):
        """
        delay to control fps with frame skiping

        if we don't have enough time to delay, we'll skip some frames
        :param fps: frames per second (max is 1000)
        :param max_skip_count: max num of  frames to skip
        """
        nanotime = 1000000000 // fps
        if self._last_update_time == 0:
            self._last_update_time = time.time_ns()
        nowtime = time.time_ns()
        if self._last_update_time + nanotime < nowtime:
            # we don't have to draw this frame, so let's skip it
            self._skip_count += 1
            if self._skip_count < max_skip_count:
                self._last_update_time = time.time_ns()
                return
            else:
                # we have skipped too many frames, draw this frame
                self._skip_count = 0
        while time.time_ns() - self._last_update_time < nanotime:
            time.time_ns()
        self.real_update()

    def get_char(self) -> str:
        """
        get the ascii char inputted by keybord
        if not any char key is pressed in last 100 ms, the program will stop and wait for the next key hitting

        :return: the character inputted by keybord
        """
        nt = time.time_ns()
        if nt - self._key_char_msg.get_time() > 100000000:
            # if the last char msg is 100ms ago, we wait for a new msg
            self._char_key_event.clear()
            self._char_key_event.wait()
        if not self._is_run:
            return ' ';
        ch = self._key_char_msg.get_char()
        self._key_char_msg.reset()
        return ch

    def get_key(self) -> (int, int):
        """
        get the key inputted by keybord
        if not any  key is pressed in last 100 ms, the program will stop and wait for the next key hitting

        :return: keyboard code (see http://pyqt.sourceforge.net/Docs/PyQt4/qt.html#Key-enum) , keyboard modifier codes(see http://pyqt.sourceforge.net/Docs/PyQt4/qt.html#KeyboardModifier-enum)
        """
        nt = time.time_ns()
        if nt - self._key_msg.get_time() > 100000000:
            # if the last key msg is 100ms ago, we wait for a new msg
            self._key_event.clear()
            self._key_event.wait()
        if not self._is_run:
            return (Qt.Key_Escape, Qt.NoModifier);
        e = self._key_msg.get_event()
        self._key_msg.reset()
        return e.key(), e.modifiers()

    def get_mouse(self) -> (int, int, int):
        """
        get the key inputted by keybord
        if not any  key is pressed in last 100 ms, the program will stop and wait for the next key hitting

        :return: x of the cursor, y of the cursor , mouse buttons down ( Qt.LeftButton or Qt.RightButton or Qt.MidButton or Qt.NoButton)
        """
        nt = time.time_ns()
        if nt - self._mouse_msg.get_time() > 100000000:
            # if the last key msg is 100ms ago, we wait for a new msg
            self._mouse_event.clear()
            self._mouse_event.wait()
        if not self._is_run:
            return (0, 0, Qt.NoButton);
        e = self._mouse_msg.get_event()
        self._mouse_msg.reset()
        return e.x(), e.y(), e.button()

    def kb_hit(self) -> bool:
        """
        see if any ascii char key is hitted in the last 100 ms
        use it with get_char()

        :return:  True if hitted, False or not
        """
        nt = time.time_ns()
        return nt - self._key_char_msg.get_time() <= 100000000

    def kb_msg(self) -> bool:
        """
        see if any key is hitted in the last 100 ms
        use it with get_key()

        :return:  True if hitted, False or not
        """
        nt = time.time_ns()
        return nt - self._key_char_msg.get_time() <= 100000000

    def mouse_msg(self) -> bool:
        """
        see if there's any mouse message(event) in the last 100 ms
        use it with get_mouse()

        :return:  True if any mouse message, False or not
        """
        nt = time.time_ns()
        return nt - self._mouse_msg.get_time() <= 100000000


class _KeyMsg:
    """
    class for saving keyboard message
    """

    def __init__(self):
        self._time = 0
        self._key_event = None

    def set_event(self, key_event: QKeyEvent):
        self._key_event = key_event
        self._time = time.time_ns()

    def get_event(self) -> QKeyEvent:
        return self._key_event

    def get_time(self) -> int:
        return self._time

    def reset(self):
        self._time = 0
        self._key_event = None


class _KeyCharMsg:
    """
    class for saving keyboard hit char
    """

    def __init__(self):
        self._time = 0
        self._key = None

    def set_char(self, key_event: QKeyEvent):
        self._key = key_event.text()
        self._time = time.time_ns()

    def get_char(self) -> str:
        return self._key

    def get_time(self):
        return self._time

    def reset(self):
        self._time = 0
        self._key = None


class _MouseMsg:
    def __init__(self):
        self._time = 0
        self._mouse_event = None

    def set_event(self, e: QMouseEvent):
        self._mouse_event = e
        self._time = time.time_ns()

    def get_event(self) -> QMouseEvent:
        return self._mouse_event

    def reset(self):
        self._time = 0
        self._mouse_event = None
