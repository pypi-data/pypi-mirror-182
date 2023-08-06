# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCookies(Component):
    """A DashCookies component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; required)

- data (string | number | list | dict; optional)

- max_age (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_cookies'
    _type = 'DashCookies'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, data=Component.UNDEFINED, max_age=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'max_age']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'max_age']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashCookies, self).__init__(**args)
