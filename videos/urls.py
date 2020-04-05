from django.conf.urls import url, re_path

from . import views

urlpatterns = [
    # re_path(r'$^', views.index, name='index'),
    re_path(r'^(?P<vid>.*)$', views.index, name='index'),
    
    # url('', views.index, name='index'),    
]
