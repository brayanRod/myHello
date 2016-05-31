#import modulos
from django.http import HttpResponse
import datetime

#definir una funcion que crear una pàgina web

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body> Hello World. The time: %s </body></html>" %now
    return HttpResponse(html)
