# -*- coding: utf-8 -*-

from interlegis.portalmodelo.buscadores.config import PROJECTNAME
from interlegis.portalmodelo.buscadores.interfaces import IBrowserLayer
from interlegis.portalmodelo.buscadores.testing import FUNCTIONAL_TESTING
from interlegis.portalmodelo.buscadores.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers
from Products.GenericSetup.upgrade import listUpgradeSteps

import unittest


class Plone43TestCase(unittest.TestCase):

    layer = FUNCTIONAL_TESTING


class BaseTestCase(unittest.TestCase):
    """Base test case to be used by other tests."""

    layer = INTEGRATION_TESTING

    profile = 'interlegis.portalmodelo.buscadores:default'

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.wt = self.portal['portal_workflow']
        self.st = self.portal['portal_setup']


class TestInstall(BaseTestCase):
    """Ensure product is properly installed."""

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())

    def test_version(self):
        self.assertEqual(
            self.st.getLastVersionForProfile(self.profile),
            (u'1000',)
        )


class TestUpgrade(BaseTestCase):
    """Ensure product upgrades work."""

    def test_to1010_available(self):

        upgradeSteps = listUpgradeSteps(self.st,
                                        self.profile,
                                        '1000')
        step = [step for step in upgradeSteps
                if (step[0]['dest'] == ('1010',))
                and (step[0]['source'] == ('1000',))]
        self.assertEqual(len(step), 1)


class TestUninstall(BaseTestCase):
    """Ensure product is properly uninstalled."""

    def test_uninstalled(self):
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browser_layer_removed_uninstalled(self):
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertNotIn(IBrowserLayer, registered_layers())
