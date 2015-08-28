# coding: utf-8

"""
    django find&replace
    ~~~~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, print_function

from django.views.generic import FormView

from .forms import FindReplaceForm


class FindAndReplace(FormView):
    form_class = FindReplaceForm
    template_name = 'find_and_replace/form.html'

    def form_valid(self, form):
        raise NotImplementedError
