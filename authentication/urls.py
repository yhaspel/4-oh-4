from django.conf.urls import url
from . import views

app_name = "authentication"
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^reqister/$', views.reqister_user, name="password_change"),
    # url(r'^password_change/done/$', views.password_change_done, name="password_change_done"),
    # url(r'^password_reset/$', views.password_reset, name="password_reset"),
    # url(r'^password_reset/done/$', views.password_reset_done, name="password_reset_done"),
]
