from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from . import models


# Create your views here.
def get_random_tip(request):
    tip = models.TipOfDay.objects.order_by("?").first()
    return get_tip(request, tip.id)


def get_tip(request, pk):
    tip = get_object_or_404(models.TipOfDay, id=pk)
    return render(request, "tips/tip.html", {
            'object': tip,
        })
