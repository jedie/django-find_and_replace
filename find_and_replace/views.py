
from django.views.generic import FormView

from .forms import FindReplaceForm


class FindAndReplace(FormView):
    form_class = FindReplaceForm
    template_name = 'find_and_replace/form.html'

    def form_valid(self, form):
        raise NotImplementedError
