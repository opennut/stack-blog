from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.logout_on, name="logout"),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', 
    	{'template_name': 'changepassword.html',
        'post_change_redirect' : 'home'}, 
        name="password_change"),
]
