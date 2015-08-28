# coding: utf-8

"""
    find&replace
    ~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""
from django.conf import settings
from django.db import models
from django.db.models.loading import get_apps, get_models
from django.utils.translation import get_language
from django import forms
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _


from find_and_replace.settings import FIND_AND_REPLACE_APP_LABELS, \
    FIND_AND_REPLACE_FIELDS
from find_and_replace.utils import get_filtered_field_choices


def get_model_fields():
    return tuple([getattr(models, field_name) for field_name in FIND_AND_REPLACE_FIELDS])


def field_choices():
    return get_filtered_field_choices(
        app_labels=FIND_AND_REPLACE_APP_LABELS,
        model_fields=get_model_fields(),
    )


class FindReplaceForm(forms.Form):
    find_string = forms.CharField(min_length=1)
    replace_string = forms.CharField(required=False)

    model_fields = forms.MultipleChoiceField(
        help_text=_("Model fields to apply find&replace")
    )

    # content_type = forms.ChoiceField(
    #     choices=CONTENT_TYPES_CHOICES,
    #     help_text=_("Please select the content type for the operation.")
    # )
    languages = forms.MultipleChoiceField(
        help_text=_("Limit the language. (Would not be used for any content type.)")
    )
    sites = forms.MultipleChoiceField(
        # choices= Set in __init__, so the Queryset would not execute at startup
        help_text=_("Limit to these sites")
    )

    simulate = forms.BooleanField(
        initial=True, required=False,
        help_text=_("Don't replace anything.")

    )

    def __init__(self, *args, **kwargs):
        super(FindReplaceForm, self).__init__(*args, **kwargs)

        self.fields["model_fields"].choices = field_choices()

        self.fields["languages"].choices = settings.LANGUAGES
        language_code=get_language()
        self.fields["languages"].initial = [language_code]

        self.fields["sites"].choices = Site.objects.all().values_list("id", "name")
        self.fields["sites"].initial = [Site.objects.get_current().id]
