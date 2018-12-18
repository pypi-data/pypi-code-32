# generated by eelbrain/scripts/make_example_tests.py
from importlib import import_module
import logging
import os
import re
import shutil
from tempfile import mkdtemp

import mne
import pytest

from eelbrain import configure

# exclude files with those names:
EXCLUDE = ('make_reports.py',)
DATASETS = {
    'mne_sample': bool(mne.datasets.sample.data_path(download=False))
}

dir_ = os.path.dirname(__file__)
examples_dir = os.path.join(dir_, '..', '..', 'examples')
examples_dir = os.path.abspath(examples_dir)
# find examples
examples = []
for dirpath, _, filenames in os.walk(examples_dir):
    relpath = os.path.relpath(dirpath, examples_dir)
    for filename in filenames:
        if filename.endswith('.py') and filename not in EXCLUDE:
            example_path = os.path.join(dirpath, filename)
            example_name = os.path.join(relpath, filename)
            examples.append((example_path, example_name))


@pytest.mark.parametrize("path,name", examples)
def test_example(path, name):
    "Run the example script at ``filename``"
    orig_wd = os.getcwd()
    dirname, example_filename = os.path.split(path)

    # read example
    with open(path) as fid:
        text = fid.read()

    # check for explicit skip
    if re.findall("^# skip test:", text, re.MULTILINE):
        return

    # check for required modules
    required_modules = re.findall("^# requires: (\w+)$", text, re.MULTILINE)
    for module in required_modules:
        print(repr(module))
        try:
            import_module(module)
        except ImportError:
            pytest.skip(f"required module {module} not available")

    # check for required datasets
    required_datasets = re.findall("^# dataset: (\w+)$", text, re.MULTILINE)
    for dataset in required_datasets:
        if not DATASETS[dataset]:
            raise pytest.skip(f"required dataset {dataset} not available")

    # find required files
    required_files = re.findall("^# file: (\w+.\w+)$", text, re.MULTILINE)

    # reduce computational load
    text = text.replace("n_samples = 1000", "n_samples = 2")

    # copy all files to temporary dir
    tempdir = mkdtemp()
    try:
        logging.info("Tempdir for %s at %s", name, tempdir)
        for filename in required_files:
            src = os.path.join(dirname, filename)
            logging.info(" Copying %s", filename)
            shutil.copy(src, tempdir)

        # execute example
        os.chdir(tempdir)
        logging.info(" Executing %s", name)
        configure(show=False)
        exec(text, {})
    finally:
        os.chdir(orig_wd)
        # delete temporary files
        # FIXME:  on Windows (Appveyor) this raises a WindowsError indicating that the folder is being used by another process
        if os.name != 'nt':
            shutil.rmtree(tempdir)
