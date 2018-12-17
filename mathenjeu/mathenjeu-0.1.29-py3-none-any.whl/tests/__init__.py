# -*- coding: utf-8 -*-
"""
@file
@brief Shortcut to *tests*.
"""

from .qcms import simple_french_qcm


def get_game(name):
    """
    Retrieves a game.

    @param      name        game name
    @return                 game
    """
    if name in ("test_qcm1", "simple_french_qcm"):
        return simple_french_qcm()
    else:
        raise ValueError("Unknown game '{0}'".format(name))
