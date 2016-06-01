from django.forms import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from . import models
from django.core.urlresolvers import reverse_lazy, reverse

# for the err_id

import random


class EMessageView(View):
    def get(self, request, err_id):
        el = models.EMessage.objects.filter(error_code=err_id).first()

        return render(request, "emessages/preview.html", {
            'm': el
        })


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
        fields = '__all__'
        # your other Meta options


class EMessageCreate(CreateView):
    form_class = EMessageForm

    model = models.EMessage


    success_url = reverse_lazy('emessages:home')

    def get_initial(self):
        d = super().get_initial()
        return d

    def form_valid(self, form):
        form.instance.user = self.request.user
        err = form.instance.error_code
        return super().form_valid(form)


# class EMessageCreate(CreateView):
#     model = models.EMessage
#     fields = [
#         'error_code',
#         'title',
#         'description',
#         'photo',
#     ]
#
#     success_url = reverse_lazy('emessages:home')
#
#     def get_initial(self):
#         d = super().get_initial()
#         return d
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         err = form.instance.error_code
#         return super().form_valid(form)


class ListEMessageView(ListView):
    page_title = "Home"
    model = models.EMessage

    success_url = reverse_lazy('emessages:home')
    template_name = "emessages/emessage_list.html"


    def get_queryset(self):
        return super().get_queryset()  # .filter(account__user=self.request.user)
