# Generated by Django 3.1.5 on 2021-02-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mta', '0009_contact_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Packages',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
