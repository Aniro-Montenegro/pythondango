from django.conf.locale import pt
from django.http import HttpResponse
import datetime
from django.shortcuts import render


# Create your views here.

def home(request):

    html = "<!DOCTYPE html><html lang='pt-br'>  <head>    <title>Título da página</title>    <meta charset='utf-8'>  " \
           "</head>  <body>   Só Jesus Salva.  </body></html>"
    return HttpResponse(html)
