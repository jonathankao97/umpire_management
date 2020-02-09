from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def render_field(field, classes=None):
    if classes is None:
        classes = []
    widget = field.field.widget
    attrs = widget.attrs
    attrs['autocomplete'] = 'off'
    if hasattr(field.field.widget, 'input_type'):
        if widget.input_type != 'checkbox':
            classes.append('form-control')
    attrs['class'] = ' '.join(classes)
    return field


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'render_field': render_field
    })
    return env
