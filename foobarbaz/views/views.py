#from django import http
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset as django_password_reset
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from foobarbaz.models import Foo

#def foo(request):
#    context = {
#        'jobs': Job.objects.all().order_by('-start'),
#        'skills': Skill.objects.all(),
#    }
#    return render(request, 'foo.html', context)

@login_required
def index(request):
    return render(request, 'index.html', {})

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login')

def password_reset(request, post_reset_redirect):
    #print request
    rc = django_password_reset(request, post_reset_redirect=post_reset_redirect)
    #print '%s' % rc
    print dir(rc)
    return rc
    #if 'application/json' in request['META']['HTTP_ACCEPT']:
    #  #do json things
    #  return "foo"
    #else:
    #  #do html things
    #  return rc
