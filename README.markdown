# [Django Template Names](https://github.com/phpdude/django-template-names/) v0.2.0 - templates names normalization helper.

Django Template Names is a small mixin which allows you to simply normalize your CBV templates names.
 
TemplateNames mixin provides you implementation for get_template_names() which generates a tuple of templates names.

Templates names depends on app name and CBV object class name. This allows you to forget about manually editing the template_name variable every time and provides a standard automatic build of the template names.

### Installation

The simplest way to install *django-template-names* is using pip:

```
pip install django-template-names
```

### Usage
 
```
from template_names import TemplateNames

class Detail(TemplateNames, DetailView):
    ...
    pass
```

See tests.py for more insight.

### Developer

Alexandr Shurigin ([phpdude](https://github.com/phpdude/))

