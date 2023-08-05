# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LifeSpanStorage(Component):
    """A LifeSpanStorage component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; required)

- data (string | number | list | dict; optional)

- limit (number; optional)

- reload (boolean; default False)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'life_span_storage'
    _type = 'LifeSpanStorage'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, data=Component.UNDEFINED, limit=Component.UNDEFINED, reload=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'limit', 'reload']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'limit', 'reload']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(LifeSpanStorage, self).__init__(**args)
