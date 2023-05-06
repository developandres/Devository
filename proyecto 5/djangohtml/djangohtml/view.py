from django.http import HttpResponse  # Desde django importar http
from django.template import Template,Context

def plantillaHTML(request):
    arch = open('./djangohtml/Templates/index1.html')
    abr = Template(arch.read())
    arch.close()
    ctx = Context()
    document = abr.render(ctx)
    return HttpResponse(document)

def plantillaHTML1(request):
    arch = open('djangohtml/Templates/index2.html')
    abr = Template(arch.read())
    arch.close()
    ctx = Context()
    document = abr.render(ctx)
    return HttpResponse(document)