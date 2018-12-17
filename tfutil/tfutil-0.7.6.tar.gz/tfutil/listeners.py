import tensorflow as tf
from tqdm import trange

from .metrics import get_metric_name

__all__ = ['Listener']


class Listener:
    def __init__(self, name, data_gn, metric_opdefs):
        self.name = name
        self.data_gn, self.steps_per_epoch = data_gn
        self.metric_ops, self.update_ops, self.reset_ops, self.metric_phs, self.summ_metric_ops = list(
            zip(*metric_opdefs))
        self.ckpt_dir = None
        self.inputs = None
        self.labels = None
        self.is_training = None
        self.logits = None
        self.ckpt_steps = None
        self.fw = None
        self.summ_names = None
        self.summ_op = None

    def begin(self, ckpt_dir, inputs, labels, is_training, logits, ckpt_steps):
        self.ckpt_dir = ckpt_dir
        self.inputs = inputs
        self.labels = labels
        self.is_training = is_training
        self.logits = logits
        self.ckpt_steps = ckpt_steps
        logdir = f'{self.ckpt_dir}/{self.name}'
        self.fw = tf.summary.FileWriter(logdir)
        self.summ_names = ['{0}/{1}'.format(self.name, get_metric_name(m)) for m in self.metric_ops]
        self.summ_op = tf.summary.merge(self.summ_metric_ops)

    def run(self, session, global_step_value):
        session.run(self.reset_ops)
        id_checkpoint = global_step_value // self.ckpt_steps
        progress_range = trange
        progress_desc = f'{self.name} evaluation {id_checkpoint}'
        for _ in progress_range(self.steps_per_epoch, desc=progress_desc):
            xb, yb = session.run(self.data_gn)
            fd = {self.inputs: xb, self.labels: yb, self.is_training: False}
            session.run(self.update_ops, feed_dict=fd)
        metrics = session.run(self.metric_ops)
        summ = session.run(self.summ_op, feed_dict={m_ph: m for (m_ph, m) in zip(self.metric_phs, metrics)})
        for name, metric in zip(self.summ_names, metrics):
            print(f'{name}: {metric}')
        self.fw.add_summary(summ, global_step=id_checkpoint)
        self.fw.flush()

    def end(self):
        self.fw.close()
