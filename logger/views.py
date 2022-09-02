from copy import copy
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    headers = copy(request.headers)
    # for i in headers:
    #     i = str(i).replace('-', '_')
    ip = get_client_ip(request)
    meta = request.META
    
    fields = {}
    fields['IP'] = ip
    fields['Shell'] = meta['SHELL']
    fields['User agent'] = headers['User-Agent']
    fields['Accept language'] = headers['Accept-Language']
    fields['Country'] = ''

    return render(request, 'index.html', context={'fields':fields})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
