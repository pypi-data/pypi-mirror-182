# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import z3cform.locationwidget


class Z3CformLocationwidgetLayer(PloneSandboxLayer):
    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=z3cform.locationwidget)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'z3cform.locationwidget:default')


Z3CFORM_LOCATIONWIDGET_FIXTURE = Z3CformLocationwidgetLayer()

Z3CFORM_LOCATIONWIDGET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(Z3CFORM_LOCATIONWIDGET_FIXTURE,),
    name='Z3CformLocationwidgetLayer:IntegrationTesting',
)

Z3CFORM_LOCATIONWIDGET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(Z3CFORM_LOCATIONWIDGET_FIXTURE,),
    name='Z3CformLocationwidgetLayer:FunctionalTesting',
)

Z3CFORM_LOCATIONWIDGET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        Z3CFORM_LOCATIONWIDGET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name='Z3CformLocationwidgetLayer:AcceptanceTesting',
)
