# Generated by Django 3.1.4 on 2020-12-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mta', '0005_auto_20201226_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='email_id',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
