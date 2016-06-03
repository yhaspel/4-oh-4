from django.conf.urls import url
from . import views

app_name = "emessages"
urlpatterns = [
    url(r'^$', views.ListEMessageView.as_view(), name="home"),
    url(r'^preview/(?P<err_id>\d+)/$', views.preview_em, name="preview"),
    url(r'^preview/(?P<user_id>\d+)/(?P<err_id>\d+)/$', views.preview_em_end, name="end_preview"),
    url(r'^add/$', views.EMessageCreate.as_view(), name="add"),
    url(r'^delete/(?P<pk>\d+)/$', views.ErrorMessageDelete.as_view(), name="delete_em"),
]
