.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
z3cform.locationwidget
==============================================================================

Widget for graphically select location in to a map, and save cordinates into field
Based in gmaps.js library

Features
--------

- Gmaps library
- Api Key Google maps definition in control panel
- Coordinates default point definition in control panel
- You can show de coordinates field via checkbox


Usage
-----

You need to set the widget to needed fields into your form instance::

    from z3cform.locationwidget.field import LocationField
    from plone.supermodel import model


    class IMyModel(model.Schema):
       my_location_field = LocationField(
           title=_(u'Map Location'),
           description=_(u'Set the location mark on the map'),
           required=False,
       )

Translations
------------

This product has been translated into

- Catalan
- Spanish
- French

Installation
------------

Install z3cform.locationwidget by adding it to your buildout::

    [buildout]

    ...

    eggs =
        z3cform.locationwidget


and then running ``bin/buildout``
