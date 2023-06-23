# Generated by Django 3.2.13 on 2023-04-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20230407_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]