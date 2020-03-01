from django.contrib import admin
from .models import Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published']
    list_filter = ('is_published',)

admin.site.register(Video, VideoAdmin)
