# Generated by Django 3.0.6 on 2020-05-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0006_auto_20200519_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='latitude',
            field=models.FloatField(default=27.7090319),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gym',
            name='longitude',
            field=models.FloatField(default=85.2911131),
            preserve_default=False,
        ),
    ]