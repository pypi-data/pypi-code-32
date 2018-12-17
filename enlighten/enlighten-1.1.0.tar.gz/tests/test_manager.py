# -*- coding: utf-8 -*-
# Copyright 2017 - 2018 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test module for enlighten._manager
"""

import signal
import sys

from enlighten import _manager

from tests import (unittest, TestCase, mock, MockTTY, MockCounter,
                   redirect_output, OUTPUT, STDOUT_NO_FD)


TERMINAL = 'enlighten._terminal.Terminal'


# pylint: disable=missing-docstring, protected-access, too-many-statements, too-many-public-methods

class TestManager(TestCase):

    def setUp(self):
        self.tty = MockTTY()
        self.resize_sig = signal.getsignal(signal.SIGWINCH)

    def tearDown(self):
        self.tty.close()
        signal.signal(signal.SIGWINCH, self.resize_sig)

    def test_init_safe(self):
        with redirect_output('stdout', self.tty.stdout):
            # Companion stream is stderr if stream is stdout
            manager = _manager.Manager()
            self.assertIs(manager.stream, sys.stdout)
            self.assertIs(manager.term.stream, sys.stdout)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init(self):
        # Companion stream is stderr if stream is stdout
        manager = _manager.Manager()
        self.assertIs(manager.stream, sys.stdout)
        self.assertIs(manager.term.stream, sys.stdout)
        # This will fail building rpm packages since stderr is redirected
        if sys.__stderr__.isatty():
            self.assertIs(manager.companion_stream, sys.__stderr__)
            self.assertIs(manager.companion_term.stream, sys.__stderr__)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_companion_hc(self):
        # Hard-coded companion stream always wins
        manager = _manager.Manager(companion_stream=OUTPUT)
        self.assertIs(manager.companion_stream, OUTPUT)
        self.assertIs(manager.companion_term.stream, OUTPUT)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_stderr(self):
        # Companion stream is stdout if stream is stderr
        manager = _manager.Manager(stream=sys.__stderr__)
        self.assertIs(manager.stream, sys.__stderr__)
        self.assertIs(manager.term.stream, sys.__stderr__)
        # This will fail building rpm packages since stderr is redirected
        if sys.__stdout__.isatty():
            self.assertIs(manager.companion_stream, sys.__stdout__)
            self.assertIs(manager.companion_term.stream, sys.__stdout__)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_redirect(self):
        # If stdout is redirected, but stderr is still a tty, use it for companion
        with redirect_output('stdout', OUTPUT):
            manager = _manager.Manager()
            self.assertIs(manager.stream, sys.stdout)
            self.assertIs(manager.term.stream, sys.stdout)
            # This will fail building rpm packages since stderr is redirected
            if sys.__stderr__.isatty():
                self.assertIs(manager.companion_stream, sys.stderr)
                self.assertIs(manager.companion_term.stream, sys.stderr)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_stderr_redirect(self):
        # If stderr is redirected, but stdout is still a tty, use it for companion
        with redirect_output('stderr', OUTPUT):
            manager = _manager.Manager(stream=sys.stderr)
            self.assertIs(manager.stream, sys.stderr)
            self.assertIs(manager.term.stream, sys.stderr)
            # This will fail building rpm packages since stderr is redirected
            if sys.__stdout__.isatty():
                self.assertIs(manager.companion_stream, sys.stdout)
                self.assertIs(manager.companion_term.stream, sys.stdout)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_stderr_companion_hc(self):

        # Hard-coded companion stream always wins
        manager = _manager.Manager(stream=sys.__stderr__, companion_stream=OUTPUT)
        self.assertIs(manager.companion_stream, OUTPUT)
        self.assertIs(manager.companion_term.stream, OUTPUT)

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_init_hc(self):

        # Nonstandard stream doesn't get a companion stream by default
        manager = _manager.Manager(stream=OUTPUT)
        self.assertIs(manager.stream, OUTPUT)
        self.assertIs(manager.term.stream, OUTPUT)
        self.assertIsNone(manager.companion_stream)
        self.assertIsNone(manager.companion_term)

    def test_counter_and_remove(self):
        # pylint: disable=no-member,assigning-non-slot
        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
        self.assertEqual(len(manager.counters), 0)

        with mock.patch.object(manager, '_set_scroll_area') as ssa:
            counter1 = manager.counter(leave=True)
        self.assertTrue(counter1.leave)
        self.assertEqual(len(manager.counters), 1)
        self.assertEqual(manager.counters[counter1], 1)
        self.assertEqual(counter1.calls, [])
        self.assertEqual(ssa.call_count, 1)

        with mock.patch.object(manager, '_set_scroll_area') as ssa:
            counter2 = manager.counter(leave=False)
        self.assertFalse(counter2.leave)
        self.assertEqual(len(manager.counters), 2)
        self.assertEqual(manager.counters[counter1], 2)
        self.assertEqual(manager.counters[counter2], 1)
        self.assertEqual(counter1.calls,
                         ['clear(flush=False)', 'refresh(flush=False, elapsed=None)'])
        self.assertEqual(counter2.calls, [])
        self.assertEqual(ssa.call_count, 1)
        counter1.calls = []

        with mock.patch.object(manager, '_set_scroll_area') as ssa:
            counter3 = manager.counter(leave=False)
        self.assertFalse(counter3.leave)
        self.assertEqual(len(manager.counters), 3)
        self.assertEqual(manager.counters[counter1], 3)
        self.assertEqual(manager.counters[counter2], 2)
        self.assertEqual(manager.counters[counter3], 1)
        self.assertEqual(counter1.calls,
                         ['clear(flush=False)', 'refresh(flush=False, elapsed=None)'])
        self.assertEqual(counter2.calls,
                         ['clear(flush=False)', 'refresh(flush=False, elapsed=None)'])
        self.assertEqual(counter3.calls, [])
        self.assertEqual(ssa.call_count, 1)
        counter1.calls = []
        counter2.calls = []

        manager.remove(counter3)
        self.assertEqual(len(manager.counters), 2)
        self.assertFalse(counter3 in manager.counters)

        # Remove again, no error
        manager.remove(counter3)
        self.assertEqual(len(manager.counters), 2)

        manager.remove(counter1)
        self.assertEqual(len(manager.counters), 2)
        self.assertTrue(counter1 in manager.counters)

        with mock.patch.object(manager, '_set_scroll_area') as ssa:
            counter4 = manager.counter(leave=False)
        self.assertFalse(counter4.leave)
        self.assertEqual(len(manager.counters), 3)
        self.assertEqual(manager.counters[counter1], 3)
        self.assertEqual(manager.counters[counter2], 2)
        self.assertEqual(manager.counters[counter4], 1)
        self.assertEqual(counter1.calls, [])
        self.assertEqual(counter2.calls, [])
        self.assertEqual(counter4.calls, [])
        self.assertEqual(ssa.call_count, 1)

    def test_counter_position(self):
        manager = _manager.Manager(stream=self.tty.stdout, set_scroll=False)
        counter1 = manager.counter(position=4)
        self.assertEqual(manager.counters[counter1], 4)

        with self.assertRaisesRegex(ValueError, 'Counter position 4 is already occupied'):
            manager.counter(position=4)

        with self.assertRaisesRegex(ValueError,
                                    'Counter position 200 is greater than terminal height'):
            manager.counter(position=200)

    def test_inherit_kwargs(self):
        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter,
                                   unit='knights', not_real=True, desc='Default')

        self.assertTrue('unit' in manager.defaults)
        self.assertTrue('desc' in manager.defaults)
        self.assertTrue('not_real' in manager.defaults)

        with mock.patch.object(manager, '_set_scroll_area'):
            ctr = manager.counter(desc='Huzzah')

        self.assertEqual(ctr.unit, 'knights')
        self.assertEqual(ctr.desc, 'Huzzah')
        self.assertFalse(hasattr(ctr, 'not_real'))

    def test_write(self):
        msg = 'test message'

        with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
            manager = _manager.Manager(stream=self.tty.stdout)
            term = manager.term
            manager.write(msg, position=3)

        self.tty.stdout.write('X\n')
        # Carriage return is getting converted to newline
        self.assertEqual(self.tty.stdread.readline(),
                         term.move(22, 0) + '\r' + term.clear_eol + msg + 'X\n')
        self.assertEqual(ssa.call_count, 1)

    def test_write_no_flush(self):
        """
        No real difference in our tests because stream is flushed on each new line
        If we don't flush, reading will just hang

        But we added this for coverage and as a framework future tests
        """

        msg = 'test message'

        with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
            manager = _manager.Manager(stream=self.tty.stdout)
            term = manager.term
            manager.write(msg, position=3, flush=False)

        self.tty.stdout.write('X\n')
        # Carriage return is getting converted to newline
        self.assertEqual(self.tty.stdread.readline(),
                         term.move(22, 0) + '\r' + term.clear_eol + msg + 'X\n')
        self.assertEqual(ssa.call_count, 1)

    def test_set_scroll_area_disabled(self):
        manager = _manager.Manager(stream=self.tty.stdout,
                                   counter_class=MockCounter, set_scroll=False)
        manager.counters['dummy'] = 3

        manager._set_scroll_area()
        self.tty.stdout.write('X\n')
        self.assertEqual(self.tty.stdread.readline(), 'X\n')

    def test_set_scroll_area_no_change(self):
        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
        manager.counters['dummy'] = 3
        manager.scroll_offset = 4

        manager._set_scroll_area()
        self.tty.stdout.write('X\n')
        self.assertEqual(self.tty.stdread.readline(), manager.term.move(21, 0) + 'X\n')

    def test_set_scroll_area_companion(self):
        """
        Ensure when no change is made, a term.move is still called for the companion stream
        """

        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter,
                                   companion_stream=self.tty.stdout)
        manager.counters['dummy'] = 3
        manager.scroll_offset = 4
        term = manager.term

        manager._set_scroll_area()
        self.tty.stdout.write('X\n')
        self.assertEqual(self.tty.stdread.readline(),
                         term.move(21, 0) + term.move(21, 0) + 'X\n')

    def test_set_scroll_area(self):
        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
        manager.counters['dummy'] = 3
        term = manager.term
        stdread = self.tty.stdread
        self.assertEqual(manager.scroll_offset, 1)
        self.assertFalse(manager.process_exit)
        self.assertNotEqual(signal.getsignal(signal.SIGWINCH), manager._resize_handler)

        with mock.patch('enlighten._manager.atexit') as atexit:
            with mock.patch.object(term, 'change_scroll'):
                manager._set_scroll_area()
                self.assertEqual(term.change_scroll.call_count, 1)  # pylint: disable=no-member

            self.assertEqual(manager.scroll_offset, 4)
            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager._resize_handler)

            self.assertEqual(stdread.readline(), term.move(24, 0) + '\n')
            self.assertEqual(stdread.readline(), '\n')
            self.assertEqual(stdread.readline(), '\n')

            self.assertTrue(manager.process_exit)

            atexit.register.assert_called_with(manager._at_exit)

        self.tty.stdout.write('X\n')
        self.assertEqual(stdread.readline(), term.move(21, 0) + 'X\n')

        # Run it again and make sure exit handling isn't reset
        with mock.patch('enlighten._manager.atexit') as atexit:
            with mock.patch.object(term, 'change_scroll'):
                manager._set_scroll_area(force=True)
                self.assertEqual(term.change_scroll.call_count, 1)  # pylint: disable=no-member

            self.assertFalse(atexit.register.called)

    def test_set_scroll_area_height(self):
        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
        manager.counters['dummy'] = 3
        manager.scroll_offset = 4
        manager.height = 20
        term = manager.term

        with mock.patch('enlighten._manager.atexit') as atexit:
            with mock.patch.object(term, 'change_scroll'):
                manager._set_scroll_area()
                self.assertEqual(term.change_scroll.call_count, 1)  # pylint: disable=no-member

            self.assertEqual(manager.scroll_offset, 4)
            self.assertEqual(manager.height, 25)
            self.assertTrue(manager.process_exit)

            term.stream.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), term.move(21, 0) + 'X\n')
            atexit.register.assert_called_with(manager._at_exit)

    def test_at_exit(self):

        tty = MockTTY()

        with mock.patch('%s.reset' % TERMINAL) as reset:
            manager = _manager.Manager(stream=tty.stdout, counter_class=MockCounter)
            term = manager.term

            # process_exit is False
            manager._at_exit()
            self.assertFalse(reset.called)
            # No output
            tty.stdout.write('X\n')
            self.assertEqual(tty.stdread.readline(), 'X\n')

            # process_exit is True, set_scroll False
            manager.process_exit = True
            manager.set_scroll = False
            manager._at_exit()
            self.assertFalse(reset.called)
            self.assertEqual(tty.stdread.readline(), term.move(25, 0) + term.cud1)

            # process_exit is True, set_scroll True
            manager.set_scroll = True
            manager._at_exit()
            self.assertEqual(reset.call_count, 1)
            self.assertEqual(tty.stdread.readline(), term.cud1)

            tty.close()
            manager._at_exit()

    def test_stop(self):

        with mock.patch('%s.reset' % TERMINAL) as reset:
            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
            manager.counters[MockCounter(manager=manager)] = 3
            manager.counters[MockCounter(manager=manager)] = 4
            term = manager.term
            self.assertIsNone(manager.companion_term)

            with mock.patch('enlighten._manager.atexit'):
                with mock.patch.object(term, 'change_scroll'):
                    manager._set_scroll_area()

            self.assertEqual(manager.scroll_offset, 5)
            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager._resize_handler)
            self.assertTrue(manager.process_exit)

            # Clear stream
            self.tty.stdout.write('X\n')
            for num in range(4 + 1):  # pylint: disable=unused-variable
                self.tty.stdread.readline()

            self.assertFalse(reset.called)
            manager.enabled = False
            manager.stop()

            # No output, No changes
            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), 'X\n')
            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager._resize_handler)
            self.assertTrue(manager.process_exit)

            manager.enabled = True
            manager.stop()

            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager.sigwinch_orig)
            self.assertEqual(reset.call_count, 1)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), term.move(23, 0) + term.clear_eol +
                             term.move(24, 0) + term.clear_eol + 'X\n')
            self.assertFalse(manager.process_exit)
            self.assertFalse(manager.enabled)
            for counter in manager.counters:
                self.assertFalse(counter.enabled)

    def test_stop_no_set_scroll(self):
        """
        set_scroll is False
        """

        with mock.patch('%s.reset' % TERMINAL) as reset:
            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter,
                                       set_scroll=False)
            manager.counters[MockCounter(manager=manager)] = 3
            manager.counters[MockCounter(manager=manager)] = 4
            term = manager.term

            with mock.patch('enlighten._manager.atexit'):
                with mock.patch.object(term, 'change_scroll'):
                    manager._set_scroll_area()

            self.assertEqual(manager.scroll_offset, 5)
            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager._resize_handler)
            self.assertTrue(manager.process_exit)

            # Stream empty
            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), 'X\n')

            manager.stop()

            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager.sigwinch_orig)
            self.assertFalse(reset.called)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), term.move(23, 0) + term.clear_eol +
                             term.move(24, 0) + term.clear_eol + term.move(25, 0) + 'X\n')
            self.assertFalse(manager.process_exit)

    def test_stop_never_used(self):
        """
        In this case, _set_scroll_area() was never called
        """

        with mock.patch('%s.reset' % TERMINAL) as reset:
            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
            manager.counters[MockCounter(manager=manager)] = 3
            manager.counters[MockCounter(manager=manager)] = 4
            self.assertFalse(manager.process_exit)

            manager.stop()

            self.assertEqual(signal.getsignal(signal.SIGWINCH), manager.sigwinch_orig)
            self.assertEqual(reset.call_count, 1)

        # No output
        self.tty.stdout.write('X\n')
        self.assertEqual(self.tty.stdread.readline(), 'X\n')

    def test_stop_companion(self):
        """
        In this case, we have a companion terminal
        Just make sure we have an extra reset
        """

        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter,
                                   companion_stream=self.tty.stdout)
        manager.counters[MockCounter(manager=manager)] = 3
        manager.counters[MockCounter(manager=manager)] = 4
        term = manager.term

        with mock.patch('enlighten._manager.atexit'):
            with mock.patch.object(term, 'change_scroll'):
                manager._set_scroll_area()

        with mock.patch.object(manager.companion_term, 'reset') as compReset:
            manager.stop()

            self.assertEqual(compReset.call_count, 1)

    def test_stop_position_1(self):
        """
        Ensure a line feed is given if there is a counter at position 1
        """

        manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)

        manager.counters[MockCounter(manager=manager)] = 3
        with mock.patch.object(manager.term, 'feed') as termfeed:
            manager.stop()
            self.assertFalse(termfeed.called)

        manager.enabled = True
        manager.counters[MockCounter(manager=manager)] = 1
        with mock.patch.object(manager.term, 'feed') as termfeed:
            manager.stop()
            self.assertTrue(termfeed.called)

    def test_resize_handler(self):

        with mock.patch('%s.width' % TERMINAL, new_callable=mock.PropertyMock) as mockheight:
            mockheight.side_effect = [80, 85, 87, 70, 70]

            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
            counter3 = MockCounter(manager=manager)
            manager.counters[counter3] = 3
            manager.scroll_offset = 4
            term = manager.term

            manager.resize_lock = True
            with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
                manager._resize_handler()
                self.assertFalse(ssa.called)

            self.assertEqual(manager.width, 80)
            self.assertTrue(manager.resize_lock)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), 'X\n')

            self.assertEqual(counter3.calls, [])

            manager.resize_lock = False
            mockheight.side_effect = [80, 85, 87, 70, 70]
            with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
                manager._resize_handler()
                self.assertEqual(ssa.call_count, 1)

            self.assertEqual(manager.width, 70)
            self.assertFalse(manager.resize_lock)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), term.move(19, 0) + term.clear_eos + 'X\n')

            self.assertEqual(counter3.calls, ['refresh(flush=False, elapsed=None)'])

    def test_resize_handler_no_change(self):

        with mock.patch('%s.width' % TERMINAL, new_callable=mock.PropertyMock) as mockheight:
            mockheight.side_effect = [80, 85, 87, 80, 80]

            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
            counter3 = MockCounter(manager=manager)
            manager.counters[counter3] = 3
            manager.scroll_offset = 4

            with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
                manager._resize_handler()
                self.assertEqual(ssa.call_count, 1)

            self.assertEqual(manager.width, 80)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), 'X\n')

            self.assertEqual(counter3.calls, ['refresh(flush=False, elapsed=None)'])

    def test_resize_handler_height_only(self):

        with mock.patch('%s.height' % TERMINAL, new_callable=mock.PropertyMock) as mockheight:
            mockheight.side_effect = [25, 23, 28, 30, 30]

            manager = _manager.Manager(stream=self.tty.stdout, counter_class=MockCounter)
            counter3 = MockCounter(manager=manager)
            manager.counters[counter3] = 3
            manager.scroll_offset = 4

            with mock.patch('enlighten._manager.Manager._set_scroll_area') as ssa:
                manager._resize_handler()
            self.assertEqual(ssa.call_count, 1)

            # Height is set in _set_scroll_area which is mocked
            self.assertEqual(manager.height, 25)

            self.tty.stdout.write('X\n')
            self.assertEqual(self.tty.stdread.readline(), 'X\n')

            self.assertEqual(counter3.calls, ['refresh(flush=False, elapsed=None)'])

    def test_disable(self):
        mgr = _manager.Manager(stream=self.tty.stdout, enabled=False)
        self.assertFalse(mgr.enabled)
        ctr = mgr.counter()
        self.assertIsInstance(ctr, _manager.Counter)
        self.assertFalse(ctr.enabled)

        # Make sure this doesn't error
        ctr.update()
        ctr.update(4)
        ctr.refresh()
        ctr.close()
        ctr.leave = False
        ctr.close()

        mgr.write()
        mgr.stop()

        # No Output
        self.tty.stdout.write('X\n')
        self.assertEqual(self.tty.stdread.readline(), 'X\n')

    def test_context_manager(self):

        mgr = None

        with _manager.Manager(stream=self.tty.stdout) as manager:
            self.assertIsInstance(manager, _manager.Manager)
            self.assertTrue(manager.enabled)
            mgr = manager

        self.assertFalse(mgr.enabled)

    def test_no_resize_signal(self):

        # Test normal case initialization
        stdmgr = _manager.Manager(stream=self.tty.stdout)
        self.assertTrue(hasattr(stdmgr, 'sigwinch_orig'))
        stdmgr.counters[MockCounter(manager=stdmgr)] = 3
        stdmgr.counters[MockCounter(manager=stdmgr)] = 4

        # Test no resize signal initialization
        with mock.patch.object(_manager, 'RESIZE_SUPPORTED', False):
            manager = _manager.Manager(stream=self.tty.stdout)
            self.assertFalse(hasattr(manager, 'sigwinch_orig'))

            manager.counters[MockCounter(manager=manager)] = 3
            manager.counters[MockCounter(manager=manager)] = 4

        # Test set_scroll_area()
        with mock.patch.object(_manager.signal, 'signal',
                               wraps=_manager.signal.signal) as mocksignal:
            with mock.patch('enlighten._manager.atexit'):

                # Test no resize signal set_scroll_area
                with mock.patch.object(_manager, 'RESIZE_SUPPORTED', False):
                    with mock.patch.object(manager.term, 'change_scroll'):
                        manager._set_scroll_area()

                self.assertFalse(mocksignal.called)

                # Test normal case set_scroll_area
                with mock.patch.object(stdmgr.term, 'change_scroll'):
                    stdmgr._set_scroll_area()
                self.assertTrue(mocksignal.called)

        # Test stop()
        with mock.patch.object(_manager.signal, 'signal',
                               wraps=_manager.signal.signal) as mocksignal:

            with mock.patch('%s.reset' % TERMINAL):

                # Test no resize signal stop
                with mock.patch.object(_manager, 'RESIZE_SUPPORTED', False):
                    manager.stop()
                self.assertFalse(mocksignal.called)

                # Test normal case stop
                stdmgr.stop()
                self.assertTrue(mocksignal.called)


class TestGetManager(TestCase):

    def setUp(self):
        self.tty = MockTTY()

    def tearDown(self):
        self.tty.close()

    def test_get_manager_tty(self):

        # stdout is attached to a tty
        with redirect_output('stdout', self.tty.stdout):
            self.assertTrue(sys.stdout.isatty())
            manager = _manager.get_manager(unit='knights')
            self.assertIsInstance(manager, _manager.Manager)
            self.assertTrue('unit' in manager.defaults)
            self.assertTrue('enabled' in manager.defaults)
            self.assertTrue(manager.enabled)
            self.assertTrue(manager.defaults['enabled'])

    @unittest.skipIf(STDOUT_NO_FD, 'No file descriptor for stdout')
    def test_get_manager_notty(self):

        # stdout is not attached to a tty
        with redirect_output('stdout', OUTPUT):
            self.assertFalse(sys.stdout.isatty())
            manager = _manager.get_manager(unit='knights')
            self.assertIsInstance(manager, _manager.Manager)
            self.assertTrue('unit' in manager.defaults)
            self.assertFalse(manager.enabled)
            self.assertTrue('enabled' in manager.defaults)
            self.assertFalse(manager.defaults['enabled'])
