from django.conf.urls import url
from . import views

app_name = "tips"

urlpatterns = [
    url(r'^rand/', views.get_random_tip, name='rand'),
    url(r'^(?P<pk>[0-9]+)/', views.get_tip, name='tip'),
    url(r'^add/', views.TipsOfDayCreate.as_view()),
    url(r'^edit/(?P<pk>[0-9]+)/', views.tips_of_days_form)
]
