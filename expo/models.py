from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.safestring import mark_safe

# Create your models here.
class Expo(models.Model):
    expo_id = models.AutoField(primary_key=True)
    expo_type_id = models.IntegerField(blank=True, null=True)
    expo_name = models.CharField(max_length=255, null=True, verbose_name='name')
    expo_place_id = models.IntegerField(blank=True, null=True)
    expo_startdate = models.DateTimeField(null=True, verbose_name='start date')
    expo_enddate = models.DateTimeField(null=True, verbose_name='end date')
    expo_info_l1 = models.TextField(blank=True, null=True, verbose_name='info_nl')
    expo_info_l2 = models.TextField(blank=True, null=True, verbose_name='info_en')
    expo_publish = models.BooleanField(null=True, verbose_name='published?')

    expo_image = models.FileField(null=True, verbose_name='image', upload_to='images',
                                    help_text='Op de website komt het plaatje eruit te zien zoals hieronder (qua grootte)')

    class Meta:
        managed = False
        db_table = 'library_expo'

    def get_date_info(self):
        dateformat = "%d %B, %Y"
        start = datetime.strftime(self.expo_startdate, dateformat)
        if (self.expo_enddate):
            end = datetime.strftime(self.expo_enddate, dateformat)
            return "{} - {}".format(start, end)
        return start

    # display an image thumbnail in the admin
    def admin_thumbnail(self):
        if self.expo_image:
            image = self.get_image_filepath()
            return mark_safe(
                '<img src="{}{}" width="256px"" />'.format(
                    settings.MEDIA_URL, image))
        else:
            return ''

    def get_image_filepath(self):
        if self.expo_image:
            image = self.expo_image
            if 'images' not in image.name:
                if not image.name.startswith('/'):
                   image = "/{}".format(image)
                image = "images{}".format(image)
            return image

    def __str__(self):
        return self.expo_name