import os
import io
import time
import requests
import imageio
import numpy as np
import pandas as pd

def mnist_tibetan(root):
    """Tibetan-MNIST from https://github.com/bat67/TibetanMNIST.
    
    Tibetan-MNIST is a drop-in replacement for the
    MNIST dataset (28x28 grayscale, 70,000 images), 
    provided in the original MNIST format as well as a NumPy format.
    Since MNIST restricts us to 10 classes, we chose one character to
    represent each of the 10 rows of Hiragana when creating Tibetan-MNIST.
    
    Each sample is an gray image (in 3D NDArray) with shape (28, 28, 1).
    
    Data storage directory:
    root = `/user/.../mydata`
    mnist data: 
    `root/mnist_tibetan/train/0/xx.png`
    `root/mnist_tibetan/train/2/xx.png`
    `root/mnist_tibetan/train/6/xx.png`
    `root/mnist_tibetan/test/0/xx.png`
    `root/mnist_tibetan/test/2/xx.png`
    `root/mnist_tibetan/test/6/xx.png`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/mnist_tibetan`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/mnist_tibetan`.
    """
    start = time.time()
    print('Downloading data from https://github.com/Hourout/datasets/TibetanMNIST')
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'mnist_tibetan')
    url_list = ['https://raw.githubusercontent.com/Hourout/datasets/master/TibetanMNIST/TibetanMNIST_28_28_01.csv',
                'https://raw.githubusercontent.com/Hourout/datasets/master/TibetanMNIST/TibetanMNIST_28_28_02.csv']
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    data = pd.DataFrame()
    for url in url_list:
        s = requests.get(url).content
        data = pd.concat([data, pd.read_csv(io.StringIO(s.decode('utf-8')),header=None, dtype='uint8')])
    train = data.loc[:, 1:].values.reshape(-1, 28, 28)
    train_label = data.loc[:, 0].values
    for i in set(train_label):
        tf.gfile.MakeDirs(os.path.join(task_path, 'train', str(i)))
    for idx in range(train.shape[0]):
        imageio.imsave(os.path.join(task_path, 'train', str(train_label[idx]), str(idx)+'.png'), train[idx])
    print('mnist_tibetan dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
