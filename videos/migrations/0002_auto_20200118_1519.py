# Generated by Django 3.0 on 2020-01-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(max_length=10000),
        ),
    ]
