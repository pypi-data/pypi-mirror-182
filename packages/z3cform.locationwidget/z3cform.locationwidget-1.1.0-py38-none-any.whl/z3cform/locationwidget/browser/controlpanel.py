# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.autoform import directives
from plone.z3cform import layout
from z3cform.locationwidget import _
from z3cform.locationwidget.widget import LocationFieldWidget
from zope import schema
from zope.interface import Interface


class ILocationwidgetControlPanel(Interface):
    directives.widget('map_center', LocationFieldWidget)
    map_center = schema.TextLine(
        title=_(u'Map center'),
        description=_(u'Set a point to initialize widget maps.'),
        default=u'0|0',
    )

    api_key = schema.TextLine(
        title=_(u'Google Maps Api key'),
        description=_(
            u'Define a key to use. Get one: https://developers.google.com/maps/documentation/javascript/get-api-key'),
        default=u'????',
    )


class LocationwidgetControlPanelForm(RegistryEditForm):
    schema = ILocationwidgetControlPanel
    schema_prefix = 'locationwidget'
    label = _(u'Location Widget Settings')


LocationwidgetControlPanelView = layout.wrap_form(LocationwidgetControlPanelForm, ControlPanelFormWrapper)
