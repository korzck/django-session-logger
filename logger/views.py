from copy import copy
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    headers = copy(request.headers)
    for i in headers:
        i = str(i).replace('-', '_')
    ip = get_client_ip(request)
    meta = request.META

    return render(request, 'index.html', context={'headers': headers, 'meta':meta, 'ip':ip})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
