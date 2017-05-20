"""Forms for the main app"""
# pylint: disable=W0232, R0903
import os
import yaml
from collections import OrderedDict

from django import forms
from django.conf import settings
from django.utils.text import slugify
from django.utils.safestring import mark_safe

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django_select2.forms import (
    Select2MultipleWidget, HeavySelect2Widget, Select2Widget, ModelSelect2Widget
)

from common.util import get_auto_increment_slug
from ingame_api import models
from games.util.installer import validate_installer


class AchievementForm(forms.ModelForm):
    class Meta(object):
        model = models.Achievement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AchievementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.add_input(Submit('submit', "Submit"))

class StatForm(forms.ModelForm):
    class Meta(object):
        model = models.Stat
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.add_input(Submit('submit', "Submit"))
