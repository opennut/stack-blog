from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    #url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.logout_on, name="logout"),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', 
    	{'template_name': 'changepassword.html',
        'post_change_redirect' : 'home'}, 
        name="password_change"),
    url(r'^users/$', views.UserListView.as_view(), name="users_list"),
    url(r'^', include('allauth.urls')),
    url(r'^profile/(?P<id>\d+)/$', views.profile.as_view(), name="profile"),
    url(r'^editprofile/$', views.user_upprofile.as_view(), name="profileedit"),
    url(r'^editimage/(?P<id>\d+)/$', views.upload_file, name="imageedit"),
    url(r'^profile/super_user/(?P<id>\d+)/$', views.super_user, name="super_user"),
    url(r'^profile/staff/(?P<id>\d+)/$', views.staff, name="staff"),
    url(r'^profile/active/(?P<id>\d+)/$', views.active, name="active"),
    url(r'^profile/inactive/(?P<id>\d+)/$', views.inactive, name="inactive"),
    url(r'^registered/$', views.registered, name="registered"),

    
]
