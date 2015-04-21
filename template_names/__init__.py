import re

__version__ = (0, 1, 0)

_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile('([a-z0-9])([A-Z])')


def get_app_template_folder(module):
    m = module.split('.')
    if not m:
        return ''

    return (m[-2] if m[-1] == 'views' else m[1]).lower()


def camel_to_snake(s):
    subbed = _underscorer1.sub(r'\1_\2', s)
    return _underscorer2.sub(r'\1_\2', subbed).lower()


class TemplateNames(object):
    template_name = None

    def get_template_exts(self):
        return ['html', 'jinja']

    def get_template_names(self):
        if not getattr(self, 'template_name', None):
            return self._generate_normalized_template_names()

        return [self.template_name]

    def _generate_normalized_template_names(self):
        module = get_app_template_folder(self.__module__)
        template = camel_to_snake(self.__class__.__name__)

        return tuple("%s/%s.%s" % (module, template, ext) for ext in self.get_template_exts())
