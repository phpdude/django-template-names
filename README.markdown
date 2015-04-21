# [Django Template Names](https://github.com/phpdude/django-template-names/) v0.1.0 - templates names normalization helper.

Django Template Names is small mixin which allows you simply normalize your CBV templates names.
 
TemplateNames mixin provide you implementation for get_template_names() which generates tuple of templates names.
Templates names depends on app name and CBV object class name. This allows you forget about manual editing
template_name variable everytime and make templates names standard way built.

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

### Developer

Alexandr Shurigin ([phpdude](https://github.com/phpdude/))

