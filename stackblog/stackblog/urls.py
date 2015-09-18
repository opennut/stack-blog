from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'stackblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/', include("questions.urls")),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^', include("home.urls")),
]
