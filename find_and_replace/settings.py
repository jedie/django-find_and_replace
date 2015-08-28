# coding: utf-8

from django.conf import settings


FIND_AND_REPLACE_APP_LABELS = getattr(settings, "FIND_AND_REPLACE_APP_LABELS",
    ("cms","djangocms_text_ckeditor",)
)

FIND_AND_REPLACE_FIELDS = getattr(settings, "FIND_AND_REPLACE_FIELDS",
    ("TextField", "CharField")
)
