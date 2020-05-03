from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from PIL import Image

class Category(models.Model):
    l_art_cat_id = models.AutoField(primary_key=True)
    l_art_cat_l1 = models.CharField(
        max_length=50, null=True, verbose_name='name_nl')
    l_art_cat_l2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='name_en')

    class Meta:
        managed = False
        db_table = 'l_art_category'

    def __str__(self):
        if self.l_art_cat_l1:
            return self.l_art_cat_l1
        return 'UNKNOWN'


class Type(models.Model):
    l_art_type_id = models.AutoField(primary_key=True)
    l_art_type_l1 = models.CharField(
        max_length=50, null=True, verbose_name='name_nl')
    l_art_type_l2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='name_en')

    class Meta:
        managed = False
        db_table = 'l_art_type'

    def __str__(self):
        if self.l_art_type_l1:
            return self.l_art_type_l1
        return 'UNKNOWN'


class Work(models.Model):    
    art_id = models.AutoField(primary_key=True)
    art_m_nr = models.IntegerField(blank=True, null=True)
    art_cat = models.ForeignKey(
        null=True, to=Category, on_delete=models.DO_NOTHING)
    art_type = models.ForeignKey(
        null=True, to=Type, on_delete=models.DO_NOTHING)
    art_title_l1 = models.CharField(
        max_length=150, null=True, verbose_name='title_nl')
    art_title_l2 = models.CharField(max_length=150, blank=True, null=True, verbose_name='title_en')
    art_serie_id = models.IntegerField(blank=True, null=True)
    art_expo_id = models.IntegerField(blank=True, null=True)
    art_material_l1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='materials_nl')
    art_material_l2 = models.CharField(max_length=150, blank=True, null=True, verbose_name='materials_en')
    art_dimension = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='dimension')
    art_date = models.DateField(max_length=255, null=True, verbose_name='date', help_text="In een van twee formaten: 'YYYY/MM/dd' of 'YYYY-MM-dd'")
    art_info_l1 = models.TextField(null=True, blank=True, verbose_name='info_nl')
    art_info_l2 = models.TextField(blank=True, null=True, verbose_name='info_en')
    art_price = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='price')
    art_sold = models.BooleanField(blank=True, null=True, verbose_name='sold')
    art_sold_to_date = models.DateTimeField(blank=True, null=True)
    art_sold_to_id = models.IntegerField(blank=True, null=True)
    art_filename = models.FileField(null=True, verbose_name='image', upload_to='images',
                                    help_text='Merk op dat een plaatje op de website getoond wordt op de grootte die je upload (zie hieronder als voorbeeld)')
    art_publish = models.BooleanField(null=True, verbose_name='published?')
    art_designer = models.CharField(max_length=255, blank=True, null=True)
    art_artist = models.CharField(max_length=255, blank=True, null=True)
    art_artist_worked_with = models.TextField(
        blank=True, null=True, verbose_name='collaborators')
    art_owned_by = models.CharField(max_length=255, blank=True, null=True)
    art_sold_info = models.TextField(blank=True, null=True)
    art_anecdote_publish = models.BooleanField(
        blank=True, null=True, verbose_name='anecdote_published?')
    art_anecdote_l1 = models.TextField(
        blank=True, null=True, verbose_name='anecdote_nl')
    art_anecdote_l2 = models.TextField(blank=True, null=True, verbose_name='anecdote_en')
    art_equipment = models.TextField(blank=True, null=True)
    art_viewable = models.IntegerField(blank=True, null=True)
    art_view_location = models.CharField(max_length=255, blank=True, null=True)
    art_view_time = models.CharField(max_length=255, blank=True, null=True)
    

    # custom prop for PIL instance
    pil_instance = None

    class Meta:
        managed = False
        db_table = 'library_art'

    def __str__(self):
        if self.art_title_l1:
            return self.art_title_l1
        return 'UNKNOWN'

    # display an image thumbnail in the admin
    def admin_thumbnail(self):
        if self.art_filename:
            image = self.get_image_filepath()
            return mark_safe(
                '<img src="{}{}" width="{}" height="{}" />'.format(
                    settings.MEDIA_URL, image, self.get_image_width, self.get_image_height))
        else:
            return ''

    def get_image_filepath(self):
        if self.art_filename:
            image = self.art_filename
            if 'images' not in image.name:
                if not image.name.startswith('/'):
                   image = "/{}".format(image)
                image = "images{}".format(image)
            return image

    def get_image_width(self):
        if not self.pil_instance:
            self.pil_instance = Image.open("media/{}".format(self.get_image_filepath()))
        return self.pil_instance.width

    def get_image_height(self):
        if not self.pil_instance:
            self.pil_instance = Image.open("media/{}".format(self.get_image_filepath()))
        return self.pil_instance.height

    def get_thumbnail_width(self):
        if not self.pil_instance:
            self.pil_instance = Image.open("media/{}".format(self.get_image_filepath()))
        width, height = self.pil_instance.size
        scale = 215 / height 
        return width * scale    

    admin_thumbnail.short_description = 'Current image'
