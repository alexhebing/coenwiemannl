from django.contrib import admin
from .models import Category, Type, Work

class CategoryAdmin(admin.ModelAdmin):
    fields = ['l_art_cat_l1']

class TypeAdmin(admin.ModelAdmin):
    fields = ['l_art_type_l1']

class WorkAdmin(admin.ModelAdmin):
    fields = [
        'art_title_l1',
        'art_title_l2',
        'art_filename',
        'admin_thumbnail', 
        'art_cat', 
        'art_type',
        'art_date',
        'art_publish',
        'art_material_l1',
        'art_material_l2', 
        'art_dimension',
        'art_info_l1',
        'art_info_l2',
        'art_price',
        'art_sold',
        'art_artist_worked_with',
    ]
    list_display = ['art_title_l1', 'art_date', 'art_publish']
    readonly_fields = ('admin_thumbnail',)
    list_filter = ('art_publish', 'art_date')


# Register your models here.
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Work, WorkAdmin)