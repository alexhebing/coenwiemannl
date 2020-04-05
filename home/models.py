from django.db import models

# Create your models here.

class HomePage(models.Model):
    text_nl = models.TextField(max_length=150000, default="hallo meiden!")
    text_en = models.TextField(max_length=150000, default="hello girls!")
