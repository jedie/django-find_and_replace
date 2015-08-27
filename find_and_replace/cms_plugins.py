# coding: utf-8

"""
    find&replace
    ~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.conf.urls import patterns, url

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .views import FindAndReplace

class FindAndReplacePlugin(CMSPluginBase):
    name = _("Find&Replace")
    render_plugin = False

    def get_plugin_urls(self):
        return patterns('',
            url(
                r'^find_and_replace/$',
                admin.site.admin_view(FindAndReplace.as_view()),
                name='find-and-replace'
            ),
        )

plugin_pool.register_plugin(FindAndReplacePlugin)
