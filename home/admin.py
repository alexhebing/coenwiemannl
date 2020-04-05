from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import HomePage

# Register your models here.
class HomePageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    
admin.site.register(HomePage, HomePageAdmin)
