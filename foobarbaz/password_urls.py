from django.conf.urls import url, include
from django.contrib import admin
from foobarbaz.views import views

password_patterns = [
    # Password Reset URLs:
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    url(r'^password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    url(r'^password_reset/complete/$',
        'django.contrib.auth.views.password_reset_complete'),
]
