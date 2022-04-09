from django.http import HttpResponse


# Create your views here.

def home(request):

    html = "<!DOCTYPE html><html lang='pt-br'>  <head>    <title>Título da página</title>    <meta charset='utf-8'>  " \
           "</head>  <body>   Só Jesus Salva.  </body></html>"
    return HttpResponse(html)
