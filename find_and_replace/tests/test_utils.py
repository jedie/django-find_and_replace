# coding: utf-8

"""
    django find&replace
    ~~~~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, print_function

from pprint import pprint

from django.db import models
from django.test import SimpleTestCase

from find_and_replace.model_fields import filter_model_fields, field_list2choices, \
    field2dot_name


class UtilsTest(SimpleTestCase):
    def test(self):
        filtered_fields = filter_model_fields(
            app_labels = ("auth", "cms"),
            model_fields = (
                models.TextField,
                models.CharField,
            )
        )
        # pprint(filtered_fields)
        # [<django.db.models.fields.CharField: name>,
        #  <django.db.models.fields.CharField: codename>,
        #  <django.db.models.fields.CharField: name>,
        #  ...
        #  <django.db.models.fields.CharField: title>,
        #  <django.db.models.fields.CharField: language>]

        field_choices = field_list2choices(filtered_fields)
        pprint(field_choices)
        # [(0, 'auth.Group.name'),
        #  (1, 'auth.Permission.codename'),
        #  (2, 'auth.Permission.name'),
        #  ...
        #  (30, 'cms.Title.title'),
        #  (31, 'cms.UserSettings.language')]

        self.assertEqual(field2dot_name(filtered_fields[2]), 'auth.Permission.name')
        self.assertEqual(field_choices[2][1], 'auth.Permission.name')

        self.assertEqual(field2dot_name(filtered_fields[30]), 'cms.Title.title')
        self.assertEqual(field_choices[30][1], 'cms.Title.title')

        self.assertEqual(len(filtered_fields), 32)
        self.assertEqual(len(field_choices), 32)