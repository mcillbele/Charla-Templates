from django.conf.urls import patterns, include, url
from views import home, ver_producto, ver_rubro

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^detalle_producto/(?P<producto_id>\d+)/', ver_producto,name='detalle'),
    url(r'^rubro/(?P<rubro_id>\d+)/', ver_rubro,name='filtro_rubro'),
)
