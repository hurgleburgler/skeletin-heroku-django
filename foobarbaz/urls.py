from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
#from django.views.generic import TemplateView
from foobarbaz.views import views

urlpatterns = patterns('',
    #url(r'^foo$', views.foo, name='foo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Password Reset URLs:
    url(r'^accounts/password_reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    (r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    (r'^accounts/password_reset/complete/$', 
        'django.contrib.auth.views.password_reset_complete'),
)
