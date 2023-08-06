# -*- coding: utf-8 -*-
from z3cform.locationwidget.interfaces import ILocationField
from zope.interface import implementer
from zope.schema import TextLine


@implementer(ILocationField)
class LocationField(TextLine):
    """ Location field """

    @property
    def lat_lng(self):
        return self.value.split('|') if self.value and '|' in self.value else None

    @property
    def lat(self):
        return self.lat_lng[0] if self.lat_lng else None

    @property
    def lng(self):
        return self.lat_lng[1] if self.lat_lng else None

    def get_lat_lng(self):
        return {'lat': self.lat_lng[0], 'lng': self.lat_lng[1]} if self.lat_lng else None
