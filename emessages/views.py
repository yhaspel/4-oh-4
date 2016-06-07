from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from authentication.models import LoggedInMixin, redirect_not_usr
from . import models
from django.core.urlresolvers import reverse_lazy
from tips import views as tips_views


def preview_em(request, err_id):
    result = redirect_not_usr(request)
    if result:
        return result
    return render(request, "emessages/preview.html",
                  {
                      'object': models.EMessage.objects.filter(error_code=err_id).first()
                  }
                  )


def preview_em_end(request, user_id, err_id):
    return render(request, "emessages/end_preview.html",
                  {
                      'object': models.EMessage.objects.filter(error_code=err_id).first()
                  }
                  )


class ErrorMessageDelete(LoggedInMixin, DeleteView):
    model = models.EMessage
    success_url = reverse_lazy('emessages:home')  # This is where this view will
    # redirect the user
    template_name = 'emessages/delete_em.html'


class EMessageForm(LoggedInMixin, ModelForm):
    def __init__(self, *args, **kwargs):
        super(EMessageForm, self).__init__(*args, **kwargs)
        self.fields['error_code'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['photo'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = models.EMessage
        fields = [
            'error_code',
            'title',
            'description',
            'photo',
        ]


class EMessageCreate(LoggedInMixin, CreateView):
    form_class = EMessageForm

    model = models.EMessage

    success_url = reverse_lazy('emessages:home')

    def get_initial(self):
        d = super().get_initial()
        return d

    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        messages.success(self.request, "Error loaded")
        return resp


class ErrorMessageUpdate(LoggedInMixin, UpdateView):
    form_class = EMessageForm

    model = models.EMessage

    success_url = reverse_lazy('emessages:home')

    def form_valid(self, form):
        messages.success(self.request, "Error updated")
        return super().form_valid(form)


class ListEMessageView(LoggedInMixin, ListView):
    page_title = "Home"
    model = models.EMessage

    success_url = reverse_lazy('emessages:home')
    template_name = "emessages/emessage_list.html"

    def get_tip(self):
        return tips_views.get_random_tip(self.request).content

    def search(self):
        return "active"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

