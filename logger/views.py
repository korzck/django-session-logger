from django.http import HttpResponse
from django.shortcuts import render
from .models import Connection

def index(request):  
    fields = {}
    fields['IP'] = get_client_ip(request)
    try:
        fields['Shell'] = request.META['SHELL']
    except:
        fields['Shell'] = 'None'
    fields['User agent'] = request.headers['User-Agent']
    fields['Accept language'] = request.headers['Accept-Language']
    fields['Country'] = ''

    connection = Connection.objects.create(
            ip=fields['IP'],
            shell = fields['Shell'],
            user_agent = fields['User agent'],
            accept_language = fields['Accept language'],
            country = fields['Country']
        )
    connection.save()

    if Connection.objects.all().count() > 100:
        for i in Connection.objects.all():
            if i.id > 100:
                i.delete()
    print(Connection.objects.all())
            

    return render(request, 'index.html', context={'fields':fields, 'connections':Connection.objects.all()[:10]})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
