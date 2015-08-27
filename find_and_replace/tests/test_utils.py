
from django.db import models
from django.db.models.loading import get_apps, get_models
from django.test import SimpleTestCase


def filter_model_fields(app_labels=None, model_fields=None):
    filtered_fields = set()
    for app in get_apps():
        for model in get_models(app):
            if app_labels is not None:
                if model._meta.app_label not in app_labels:
                    continue

            for field in model._meta.fields:
                if not isinstance(field, model_fields):
                    continue

                filtered_fields.add(field)

    return filtered_fields

def sorted_choices(fields):
    return [
        (index, '%s.%s.%s' % (
                field.model._meta.app_label, field.model._meta.object_name, field.get_attname()
            )
        )
        for index, field in enumerate(sorted(fields))
    ]



class UtilsTest(SimpleTestCase):
    def test(self):
        filtered_fields = filter_model_fields(
            app_labels = ("auth", "cms"),
            model_fields = (
                models.TextField,
                models.CharField,
            )
        )
        field_choices = sorted_choices(filtered_fields)
        import pprint
        pprint.pprint(field_choices)
        """
        [(0, 'auth.Permission.name'),
        (1, 'auth.Permission.codename'),
        (2, 'auth.Group.name'),
        (3, 'auth.User.password'),
        (4, 'auth.User.username'),
        (5, 'auth.User.first_name'),
        (6, 'auth.User.last_name'),
        (7, 'auth.User.email'),
        (8, 'cms.UserSettings.language'),
        (9, 'cms.Placeholder.slot'),
        (10, 'cms.CMSPlugin.language'),
        (11, 'cms.CMSPlugin.plugin_type'),
        (12, 'cms.Page.created_by'),
        (13, 'cms.Page.changed_by'),
        (14, 'cms.Page.reverse_id'),
        (15, 'cms.Page.navigation_extenders'),
        (16, 'cms.Page.template'),
        (17, 'cms.Page.application_urls'),
        (18, 'cms.Page.application_namespace'),
        (19, 'cms.Page.languages'),
        (20, 'cms.Title.language'),
        (21, 'cms.Title.title'),
        (22, 'cms.Title.page_title'),
        (23, 'cms.Title.menu_title'),
        (24, 'cms.Title.meta_description'),
        (25, 'cms.Title.slug'),
        (26, 'cms.Title.path'),
        (27, 'cms.Title.redirect'),
        (28, 'cms.PlaceholderReference.name'),
        (29, 'cms.StaticPlaceholder.name'),
        (30, 'cms.StaticPlaceholder.code'),
        (31, 'cms.StaticPlaceholder.creation_method')]
        """
