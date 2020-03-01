from django.conf.urls import url

from . import views

urlpatterns = [
    url('for_sale', views.for_sale, name='for_sale'),
    url('portraits', views.portraits, name='portraits'),
    url('objects', views.objects, name='objects'),
    url('surrealistic', views.surrealistic, name='surrealistic'),
    url('realistic', views.realistic, name='realistic'),
]