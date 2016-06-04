from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from authentication.models import LoggedInMixin, redirect_not_usr
from . import forms, models


def get_abulote_tip(pk=None):
    if pk == None:
        tip = models.TipOfDay.objects.order_by("?")
        if len(tip) == 0:
            tip = models.TipOfDay()
            tip.id = None
            tip.title = "No tips.. "
            tip.tip_author = "Yoni Mood"
            tip.tip_text = "run:>>>> from tips import console as mc >>>> mc.save_tips(mc.load_tips_from_dlsv())"
        else:
            tip = tip.first()
    else:
        tip = models.TipOfDay.objects.filter(pk=pk)
        if len(tip) == 0:
            tip = models.TipOfDay()
            tip.id = None
            tip.title = "404"
            tip.tip_author = "Yoni Mood"
            tip.tip_text = "there is no tip"
        else:
            tip = tip.first()
    return tip


    # Create your views here.


def get_random_tip(request):
    # result = redirect_not_usr(request)
    # if result:
    #     return result
    tip = get_abulote_tip()
    return get_tip(request, tip.id)


def tips_of_days_form(request, pk):
    result = redirect_not_usr(request)
    if result:
        return result
    pk = int(pk)
    tip = get_object_or_404(models.TipOfDay, pk=pk)
    if request.POST:
        if request.POST:
            t_form = forms.TipsForDayForm(request.POST, instance=tip)
            t_form.save()
            return redirect('emessages:home')
    t_form = forms.TipsForDayForm(instance=tip)
    return render(request, 'tips/tipofday_form.html', {'form': t_form})


class TipsOfDayCreate(LoggedInMixin, CreateView):
    form_class = forms.TipsForDayForm

    model = models.TipOfDay

    success_url = reverse_lazy('emessages:home')

    def get_initial(self):
        return super().get_initial()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def get_tip(request, pk):
    tip = get_abulote_tip(pk=pk)
    return render(request, "tips/tip.html", {
        'object': tip,
    })
