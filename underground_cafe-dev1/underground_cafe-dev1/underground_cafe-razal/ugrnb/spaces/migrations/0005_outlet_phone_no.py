# Generated by Django 2.2.4 on 2019-09-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0004_auto_20190916_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='phone_no',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
