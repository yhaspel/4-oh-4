from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView

from . import models, forms


# Create your views here.
def get_random_tip(request):
    tip = models.TipOfDay.objects.order_by("?").first()
    return get_tip(request, tip.id)


def tips_of_days_form(request, pk):
    pk = int(pk)
    tip = get_object_or_404(models.TipOfDay,pk=pk)
    if request.POST:
        if request.POST:
            t_form = forms.TipsForDayForm(request.POST, instance=tip)
            t_form.save()
            return redirect('emessages:home')
    t_form = forms.TipsForDayForm(instance=tip)
    return render(request, 'tips/tipofday_form.html', {'form': t_form})


class TipsOfDayCreate(CreateView):
    form_class = forms.TipsForDayForm

    model = models.TipOfDay

    success_url = reverse_lazy('emessages:home')

    def get_initial(self):
        return super().get_initial()

    def form_valid(self, form):
        form.instance.user = self.request.user
        err = form.instance.error_code
        return super().form_valid(form)


def get_tip(request, pk):
    tip = get_object_or_404(models.TipOfDay, id=pk)
    return render(request, "tips/tip.html", {
        'object': tip,
    })
