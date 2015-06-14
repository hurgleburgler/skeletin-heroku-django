from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
#from django.views.generic import TemplateView
from foobarbaz.views import views
from password_urls import password_patterns

urlpatterns = patterns('',
    #url(r'^foo$', views.foo, name='foo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^accounts/', include(password_patterns)),
)
