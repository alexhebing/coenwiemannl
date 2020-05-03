from django.contrib import admin

from .models import Expo

class ExpoAdmin(admin.ModelAdmin):
    fields = ['expo_name', 'expo_startdate', 'expo_enddate', 'expo_info_l1', 'expo_image', 'admin_thumbnail', 'expo_publish']
    list_display = ['expo_name', 'expo_startdate', 'expo_publish']
    list_filter = ['expo_publish']
    readonly_fields = ('admin_thumbnail',)

admin.site.register(Expo, ExpoAdmin)