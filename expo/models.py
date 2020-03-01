from django.db import models
from datetime import datetime

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

    def __str__(self):
        return self.expo_name