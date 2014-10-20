from django.shortcuts import render,render_to_response
import datetime

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from radiator.serializers import UserSerializer, GroupSerializer, AlarmSerializer
from radiator.models import Alarm
from django.db.models.query import Q
from django.http import HttpResponse
from django.template import RequestContext, loader

import datetime
import urlparse

from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db.models.query import Q
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

def requires(value_or_callable):
    def wrapped(func):
        def call(request, *args, **kwargs):
            if callable(value_or_callable):
                result = value_or_callable(request)
            else:
                result = value_or_callable
            
            if not result:
                return HttpResponseRedirect(reverse('overseer:index'))
            
            return func(request, *args, **kwargs)
        return call
    return wrapped

def respond(template, context={}, request=None, **kwargs):
    "Calls render_to_response with a RequestConext"
    from django.http import HttpResponse
    from django.template import RequestContext
    from django.template.loader import render_to_string    

    if request:
        default = context_processors.default(request)
        default.update(context)
    else:
        default = context.copy()
    
    rendered = render_to_string(template, default, context_instance=request and RequestContext(request) or None)
    return HttpResponse(rendered, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AlarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

def index(request):
    "Displays a list of all services and their current status."
    
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    #service_list = Service.objects.all()
    
    alarm_list = list(Alarm.objects\
                             .filter(Q(status__gt=0) | Q(date_updated__gte=datetime.datetime.now()-datetime.timedelta(days=1)))\
                             .order_by('-date_created')[0:6])
    
    #if alarm_list:
    #    latest_alarm, alarm_list = alarm_list[0], alarm_list[1:]
    #else:
    #    latest_alarm = None
    
    return render_to_response('radiator/index.html', {
        #'service_list': service_list,
        'alarm_list': alarm_list,
        #'latest_alarm': latest_alarm,
    }, context)

def alarm(request, id):
    "Displays a list of all services and their current status."
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    
    try:
        evt = Alarm.objects.get(pk=id)
    except Alarm.DoesNotExist:
        return HttpResponseRedirect(reverse('overseer:index'))
    
    update_list = list(evt.eventupdate_set.order_by('-date_created'))
    
    return render_to_response('radiator/alarm.html', {
        'alarm': evt,
        'update_list': update_list,
    }, context)
