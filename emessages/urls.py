from django.conf.urls import url
from . import views

app_name = "emessages"
urlpatterns = [
    url(r'^$', views.ListEMessageView.as_view(), name="home"),
    url(r'^preview/(?P<err_id>[0-9]+)/$', views.EMessageView.as_view(), name="preview"),
    url(r'^add/$', views.EMessageCreate.as_view(), name="add"),
]
