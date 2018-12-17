# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import shutil
import tempfile

import pytest


@pytest.fixture
def tmppath(request):
    """Application fixture."""
    tmppath = tempfile.mkdtemp()

    def teardown():
        shutil.rmtree(tmppath)

    request.addfinalizer(teardown)
    return tmppath
