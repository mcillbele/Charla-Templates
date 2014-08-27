# -*- coding: utf-8 -*-
from models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    productos = Producto.objects.all()
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def ver_rubro(request,rubro_id):
    productos = Producto.objects.filter(rubro=rubro_id)
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def ver_producto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render_to_response('detalle_producto.html', locals(), context_instance=RequestContext(request))
