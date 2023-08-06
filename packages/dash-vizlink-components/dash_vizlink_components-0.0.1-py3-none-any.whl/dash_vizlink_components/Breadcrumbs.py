# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Breadcrumbs(Component):
    """A Breadcrumbs component.
Breadcrumbs is a component to aid in app navigation.
It takes a list of objects, each with a `label` property,
It also takes in a value which corresponds to the label
of the currently active item.
It renders a navigation bar, with items laid out sequentially in
the order they were provided. The active item is displayed as text,
while all other items are displayed as links, which when clicked are set
as the current active item.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- activeColor (string; optional):
    The color of the active item.

- backgroundColor (string; optional):
    The background color of the bar.

- color (string; optional):
    The default color of the items.

- hoverColor (string; optional):
    The color of the link items when hovered.

- items (list of dicts; optional):
    The list of items displayed in the navigation bar.

    `items` is a list of dicts with keys:

    - label (string; optional):
        Label for the breadcrumb item.

- value (string; optional):
    The label of the active item."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vizlink_components'
    _type = 'Breadcrumbs'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, items=Component.UNDEFINED, value=Component.UNDEFINED, color=Component.UNDEFINED, activeColor=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, hoverColor=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'activeColor', 'backgroundColor', 'color', 'hoverColor', 'items', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activeColor', 'backgroundColor', 'color', 'hoverColor', 'items', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Breadcrumbs, self).__init__(**args)
