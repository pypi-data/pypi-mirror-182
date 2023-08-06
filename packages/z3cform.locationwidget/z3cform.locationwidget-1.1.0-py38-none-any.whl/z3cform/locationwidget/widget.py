# -*- coding: utf-8 -*-
from .interfaces import ILocationWidget
from DateTime import DateTime
from plone import api
from z3c.form.browser.widget import HTMLTextAreaWidget
from z3cform.locationwidget import _
from zope.interface import implementer

import z3c.form
import zope.component


@implementer(ILocationWidget)
class LocationWidget(HTMLTextAreaWidget, z3c.form.widget.Widget):
    name = 'location'
    label = _(u'Location')
    timestamp = DateTime().millis()

    @property
    def default_value(self):
        try:
            return api.portal.get_registry_record(name='locationwidget.map_center')
        except Exception:  # noqa
            return '0|0'

    @property
    def api_key(self):
        return api.portal.get_registry_record(name='locationwidget.api_key')


# @zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def LocationFieldWidget(field, request):
    return z3c.form.widget.FieldWidget(field, LocationWidget(request))
