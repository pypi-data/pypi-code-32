# WIP

import sys
import os
import logging
import warnings
import json
from datetime import datetime

import numpy as np
import torch

from  atalaya.grapher.grapher import Grapher

class _Params():
    """Class that loads hyperparameters from a json file.

    From :
    - https://cs230-stanford.github.io/logging-hyperparams.html
    - https://github.com/cs230-stanford/cs230-code-examples/blob/master/pytorch/vision/utils.py
    
    Example:
    ```
    params = Params(json_path)
    print(params.learning_rate)
    params.learning_rate = 0.5  # change the value of learning_rate in params
    ```
    """

    def __init__(self, params=None, path=None):
        if params is not None:
            self.__dict__.update(params)
        elif path is not None:
            self.update(path)
        else:
            raise Exception('params and path at None ! One of them must be not None.')

    def save(self, path):
        """Saves parameters to a json file"""
        with open(os.path.join(path, "params.json"), 'w') as f:
            json.dump(self.__dict__, f, indent=4)
            
    def update(self, path):
        """Loads parameters from json file"""
        with open(os.path.join(path, 'params.json')) as f:
            params = json.load(f)
            params[list(self.__dict__.keys())[list(self.__dict__.values()).index(path)]] = path
            self.__dict__.update(params)

    @property
    def dict(self):
        """Gives dict-like access to Params instance by `params.dict['learning_rate']"""
        return self.__dict__



class Logger:
    def __init__(self, name='exp', add_time=True, grapher='tensorboard', server='http://localhost', port=8097):
        """Logs models, optimizers, and all you want. Creates checkpoints at 
        a given frequencie and save directly the best model.
        Can also be used as a grapher to visualise graphs or images.
        """
        if add_time:
            name = '{}_{}'.format(name, datetime.now().strftime("%Y%m%d_%H%M%S"))
        self.logs_dir = os.path.join('logs', name)

        self.checkpoints_dir = os.path.join(self.logs_dir, 'checkpoints')
        self._logs_file = os.path.join(self.logs_dir, ".actions_of_logger.txt")
        self._csv_file = os.path.join(self.logs_dir, "losses.csv")

        self.params = None
        self.state = dict()

        if grapher == 'visdom':
            self.grapher = Grapher('visdom', env=name,
                                    server=server,
                                    port=port)
        elif grapher == 'tensorboard':
            self.grapher = Grapher('tensorboard', log_dir=os.path.join('visualize', name))
        else:
            raise Exception('Grapher {} is not defined. Choose between "visdom" and "tensorboard"'.format(grapher))

        self._makedirs()
        self._epoch = 0
        self.add('epoch', self._epoch)
        self._epoch_prints = True
        self._loss = sys.maxsize

        # for logging
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)

        for handler in self._logger.handlers[:]:
            self._logger.removeHandler(handler)
        
        if not self._logger.handlers:
            # Logging to a file
            _file_handler = logging.FileHandler(os.path.join(self.logs_dir, "train.log"))
            _file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
            self._logger.addHandler(_file_handler)

            # Logging to console
            _console_handler = logging.StreamHandler()
            _console_handler.setFormatter(logging.Formatter('%(message)s'))
            self._logger.addHandler(_console_handler)

    def _makedirs(self):
        """Creates the directories where logs will be stored."""
        content = 'This file contains the history of actions of logger:'
        if os.path.exists(self.logs_dir):
            raise Exception('{} directory already exists ! Put add_date to True or give another name.'.format(self.logs_dir))
        os.makedirs(self.logs_dir, exist_ok=True)
        content = "{}- creating {} directory\n".format(content, self.logs_dir)
        os.makedirs(self.checkpoints_dir, exist_ok=True)
        content = "{}- creating {} directory\n".format(content, self.checkpoints_dir)
        content = "{}- creating {} directory\n".format(content, self._logs_file)
        self._writefile(self._logs_file, content, mode='w')

    def _save(self, path):
        """Saves a state (dictionary) using torch.save()"""
        state_to_save = dict()
        self.state['epoch'] = self._epoch
        for key in self.state.keys():
            if 'state_dict' in dir(self.state[key]):
                state_to_save[key] = self.state[key].state_dict()
            else:
                state_to_save[key] = self.state[key]
        torch.save(state_to_save, path)

    def _save_parameters(self):
        """Saves parameters of the experience."""
        self.params.save(self.logs_dir)
        self._writefile(self._logs_file, '- save parameters\n')

    def _writefile(self, path, content, mode='a'):
        """Writes content to the file given by path."""
        with open(path, mode) as f:
            f.write(content)

    def add(self, name, obj, overwrite=False):
        """Adds an object to the state (dictionary)."""
        if name in self.state.keys() and not overwrite:
            raise Exception('{} is already added ! To overwrite it you have to put overwrite=True'.format(name))
        self.state[name] = obj
        self._writefile(self._logs_file, '- add : {}\n'.format(name))

    def add_scalar(self, tag, scalar_value, global_step=None):
        """Adds a scalar to the grapher."""
        self.grapher.add_scalar(tag, scalar_value, global_step)

    def add_scalars(self, main_tag, tag_scalar_dict, global_step=None):
        """Adds scalars to the grapher."""
        self.grapher.add_scalars(main_tag, tag_scalar_dict, global_step)

    def export_scalars_to_json(self, path):
        """Exports scalars to json"""
        self.grapher.export_scalars_to_json(path)

    def add_histogram(self, tag, values, global_step=None, bins='tensorflow'):
        """Add histogram to summary."""
        self.grapher.add_histogram(tag, values, global_step, bins)

    def add_image(self, tag, img_tensor, global_step=None, caption=None):
        """Add image data to summary."""
        self.grapher.add_image(tag, img_tensor, global_step, caption)

    def add_figure(self, tag, figure, global_step=None, close=True):
        """Render matplotlib figure into an image and add it to summary."""
        self.grapher.add_figure(tag, figure, global_step, close)

    def add_video(self, tag, vid_tensor, global_step=None, fps=4):
        """Add video data to summary."""
        self.grapher.add_video(tag, vid_tensor, global_step, fps)

    def add_audio(self, tag, snd_tensor, global_step=None, sample_rate=44100):
        """Add audio data to summary."""
        self.grapher.add_audio(tag, snd_tensor, global_step, sample_rate)

    def add_text(self, tag, text_string, global_step=None):
        """Add text data to summary."""
        self.grapher.add_text(tag, text_string, global_step)

    def add_graph_onnx(self, prototxt):
        self.grapher.add_graph_onnx(prototxt)

    def add_graph(self, model, input_to_model=None, verbose=False, **kwargs):
        """Adds a graph to the grapher."""
        self.grapher.add_graph(model, input_to_model, verbose, **kwargs)

    def add_embedding(self, mat, metadata=None, label_img=None,
                      global_step=None, tag='default', metadata_header=None):
        """Adds an embedding to the grapher."""
        self.grapher.add_embedding(mat, metadata, label_img, global_step, tag, metadata_header)

    def add_pr_curve(self, tag, labels, predictions, global_step=None, num_thresholds=127, weights=None):
        """Adds precision recall curve."""
        self.grapher.add_pr_curve(tag, labels, predictions, global_step, num_thresholds, weights)

    def add_pr_curve_raw(self, tag, true_positive_counts,
                         false_positive_counts,
                         true_negative_counts,
                         false_negative_counts,
                         precision,
                         recall, global_step=None, num_thresholds=127, weights=None):
        """Adds precision recall curve with raw data."""
        self.grapher.add_pr_curve_raw(tag, true_positive_counts,
                                    false_positive_counts,
                                    true_negative_counts,
                                    false_negative_counts,
                                    precision,
                                    recall, global_step, num_thresholds, weights)

    def add_parameters(self, params):
        """Adds parameters."""
        self.params = _Params(params=vars(params))
        self._save_parameters()

    def close(self):
        """Close the grapher."""
        self.grapher.close()

    def info(self, *argv):
        """Adds an info to the logging file."""
        msg = ' '.join(list(argv))
        self._logger.info(msg)

    def store(self, loss, save_every=1, overwrite=True):
        """Checks if we have to store or if the currenct model is the best. If it is the case save the best."""
        if self._epoch_prints:
            self._epoch_prints = False
            self._writefile(self._logs_file, '- save every {} epochs with overwrite = {}\n'.format(save_every, overwrite))

        best_name = 'best.pth'
        checkpoint_name = 'checkpoint_'+str(self._epoch)+'.pth'

        if overwrite:
            checkpoint_name = 'checkpoint.pth'

        if loss < self._loss:
            self._save(os.path.join(self.logs_dir, best_name))
            self._loss = loss

        if self._epoch % save_every == 0 :
            self._save(os.path.join(self.checkpoints_dir, checkpoint_name))

        self._epoch += 1

    def save(self):
        """Saves the grapher."""
        self.grapher.save()

    def register_plots(self, values, epoch, prefix='train', apply_mean=False):
        """helper to register a list of scalars."""
        for k, v in values.items():
            if isinstance(v, dict):
                self.register_plots(values[k], epoch, prefix=prefix, apply_mean=apply_mean)
            if apply_mean:
                v = np.mean(v)
                k = '{}_mean'.format(k)
            if 'mean' in k or 'scalar' in k:
                key_name = k.split('_')[0]
                value = v.item() if not isinstance(v, (int, float, np.float32, np.float64)) else v
                self.grapher.add_scalar('{}_{}'.format(prefix, key_name), value, epoch)

    def restore(self, folder=None, best=False):
        """Loads a state usinf torch.load()"""
        if best:
            path = os.path.join(self.logs_dir, 'best.pth')
        else:
            if folder == self.logs_dir:
                warnings.warn('You are loading parameters from the current directory where this experience is saved, it may leads to an error')
        
            path = os.path.join(folder, self.checkpoints_dir[len(self.logs_dir)+1:])
            checkpoint = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
            path = os.path.join(path, sorted(checkpoint)[-1])
        
        state_restored = torch.load(path)
        for key in self.state.keys():
            if 'state_dict' in dir(self.state[key]):
                self.state[key] = self.state[key].load_state_dict(state_restored[key])
            else:
                if type(self.state[key]) is list:
                    print(key)
                    self.state[key] += state_restored[key]
                elif type(self.state[key]) in [dict, set]:
                    self.state[key].update(state_restored[key])
                else:
                    self.state[key] = state_restored[key]
        
        self._epoch = self.state['epoch']
        self._writefile(self._logs_file, '\n- restored form {} at epoch {}'.format(path, self._epoch))

    def restore_parameters(self, path):
        """Loads the parameters of a previous experience given by path"""
        if path == self.logs_dir:
            warnings.warn('You are loading parameters from the current directory where this experience is saved, it may leads to an error')
        self.params.update(path)
        self._writefile(self._logs_file, '- load parameters from {}\n'.format(path))
        return self.params

    def warning(self, *argv):
        """Adds a warning to the logging file."""
        msg = ' '.join(list(argv))
        self._logger.warning(msg)

    def write_to_csv(self, *argv):
        """Write args in a csv file."""
        content = ', '.join(map(str, argv))
        content = '{}\n'.format(content)
        if os.path.isfile(self._csv_file):
            self._writefile(self._csv_file, content)
        else:
            self._writefile(self._logs_file, "- creating {} directory\n".format(self._csv_file))
            self._writefile(self._csv_file, content, mode='w')           


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Example')
    args = parser.parse_args()

    #logger = Logger(grapher='visdom')
    logger = Logger()
    logger.add_parameters(args)
    logger.info('test info 1')
    logger.warning('test warning')
    logger.info('test info 2')

    logger.add_scalar('my_scalar', 0, 1)
    logger.add_scalar('my_scalar', 1, 2)
    logger.close()
