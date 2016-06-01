from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, FormView
from . import models
from django.core.urlresolvers import reverse_lazy, reverse


class EMessageView(View):
    def get(self, request, err_id):
        el = models.EMessage.objects.filter(error_code=err_id).first()
        err = 0
        # success_url = reverse_lazy('emessages:preview', kwargs={'err_id': err})

        return render(request, "emessages/preview.html", {
            'err_id': err_id
        })


class EMessageCreate(CreateView):
    model = models.EMessage
    fields = [
        'error_code',
        'title',
        'description',
        'image URL',
    ]

    success_url = reverse_lazy('emessages:add')

    def get_initial(self):
        d = super().get_initial()
        return d

    def form_valid(self, form):
        form.instance.user = self.request.user
        err = form.instance.error_code
        return super().form_valid(form)


class ListEMessageView(ListView):
    page_title = "Home"
    model = models.EMessage

    def get_queryset(self):
        return super().get_queryset()
