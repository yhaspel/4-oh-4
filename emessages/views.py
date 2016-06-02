from django.contrib import messages
from django.forms import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from . import models
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from tips import views as tips_views

# for the err_id

def preview_em(request, err_id):
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


class EMessageForm(ModelForm):
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


class EMessageCreate(CreateView):
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


class ListEMessageView(ListView):
    page_title = "Home"
    model = models.EMessage

    success_url = reverse_lazy('emessages:home')
    template_name = "emessages/emessage_list.html"

    def get_tip(self):
        return tips_views.get_random_tip(self.request).content

    def get_queryset(self):
        return super().get_queryset()  # .filter(account__user=self.request.user)


import random
