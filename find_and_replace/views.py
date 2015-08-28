# coding: utf-8

"""
    django find&replace
    ~~~~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from __future__ import absolute_import, print_function
from django.contrib.auth import get_user_model
from django.template import RequestContext

from django.views.generic import FormView

from .forms import FindReplaceForm


class FindAndReplace(FormView):
    form_class = FindReplaceForm
    template_name = 'find_and_replace/form.html'

    def get_context_data(self, **kwargs):
        context = super(FindAndReplace, self).get_context_data(**kwargs)

        # User = get_user_model()
        # context["opts"] = User._meta
        #
        # context['change'] = "foobar"
        # context['is_popup'] = False
        # context['save_as'] = False
        #
        # context['has_delete_permission'] = False
        # context['has_add_permission'] = False
        # context['has_change_permission'] = True
        # context['show_delete'] = False
        #
        # context["adminform"] = context["form"]

        context = RequestContext(self.request, context)
        return context

    def form_valid(self, form):
        raise NotImplementedError("TODO")
