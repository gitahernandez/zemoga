# Generated by Django 3.1.6 on 2021-02-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210214_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='kind',
            field=models.CharField(default='', max_length=20),
        ),
    ]
