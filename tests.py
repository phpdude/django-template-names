import pytest

from django.views.generic.detail import DetailView

from template_names import TemplateNames, camel_to_snake, get_app_template_folder

def test_camel_to_snake():
    assert camel_to_snake('camelCaseStringExample') == 'camel_case_string_example'
    assert camel_to_snake('camelCaseString44Example') == 'camel_case_string44_example'

def test_get_app_template_folder():
    myview = CleanDetail()
    assert get_app_template_folder(myview.__module__) == 'tests'

class DetailWithTemplateProvided(TemplateNames, DetailView):
    template_name = 'somewhere/provided_template_name.html'

def test_provided_template_name():
    myview = DetailWithTemplateProvided()
    assert myview.get_template_names() == ['somewhere/provided_template_name.html',]

class CleanDetail(TemplateNames, DetailView):
    # template_name not provided manually
    pass

def test_generated_template_names():
    myview = CleanDetail()
    assert myview.get_template_names() == ('tests/clean_detail.html', 'tests/clean_detail.jinja')

class DetailWithExtensions(TemplateNames, DetailView):
    def get_template_exts(self):
        return ['html',]

def test_generated_template_names_with_extension_override():
    myview = DetailWithExtensions()
    assert myview.get_template_names() == ('tests/detail_with_extensions.html',)

