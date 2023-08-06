# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from z3c.form.interfaces import ITextWidget
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.interfaces import ITextLine


class IZ3CformLocationwidgetLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ILocationWidget(ITextWidget):
    """Marker interface that defines a browser layer."""


class ILocationField(ITextLine):
    """Marker interface that defines a browser layer."""

    def lat_lng():
        """ Array [lat, lng] """
