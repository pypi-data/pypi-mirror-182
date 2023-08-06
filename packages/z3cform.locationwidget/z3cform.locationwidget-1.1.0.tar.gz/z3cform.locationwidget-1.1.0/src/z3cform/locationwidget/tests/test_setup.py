# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from z3cform.locationwidget.testing import Z3CFORM_LOCATIONWIDGET_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that z3cform.locationwidget is properly installed."""

    layer = Z3CFORM_LOCATIONWIDGET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if z3cform.locationwidget is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'z3cform.locationwidget'))

    def test_browserlayer(self):
        """Test that IZ3CformLocationwidgetLayer is registered."""
        from z3cform.locationwidget.interfaces import (
            IZ3CformLocationwidgetLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IZ3CformLocationwidgetLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = Z3CFORM_LOCATIONWIDGET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['z3cform.locationwidget'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if z3cform.locationwidget is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'z3cform.locationwidget'))

    def test_browserlayer_removed(self):
        """Test that IZ3CformLocationwidgetLayer is removed."""
        from z3cform.locationwidget.interfaces import \
            IZ3CformLocationwidgetLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IZ3CformLocationwidgetLayer,
            utils.registered_layers())
