# Generated by Django 2.2.4 on 2019-09-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderitem_kotstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='kotstatus',
            field=models.CharField(choices=[('pending', 'pending'), (1, 'pass')], default=0, max_length=20),
        ),
    ]
