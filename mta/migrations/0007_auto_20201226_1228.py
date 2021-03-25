# Generated by Django 3.1.4 on 2020-12-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mta', '0006_home_email_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(default='main', max_length=50)),
                ('logo', models.ImageField(default='', upload_to='images')),
                ('favicon', models.ImageField(default='', upload_to='images')),
                ('phone_no', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
                ('address_l1', models.CharField(default='', max_length=50)),
                ('address_l2', models.CharField(default='', max_length=50)),
                ('address_l3', models.CharField(default='', max_length=50)),
                ('address_l4', models.CharField(default='', max_length=50)),
                ('address_l5', models.CharField(default='', max_length=50)),
                ('email_id', models.EmailField(default='', max_length=254)),
                ('hero_pink', models.CharField(default='', max_length=500)),
                ('hero_black', models.CharField(default='', max_length=500)),
                ('hero_grey_l1', models.CharField(default='', max_length=500)),
                ('hero_grey_l2', models.CharField(default='', max_length=500)),
                ('hero_grey_l3', models.CharField(default='', max_length=500)),
                ('hero_grey_l4', models.CharField(default='', max_length=500)),
                ('hero_grey_l5', models.CharField(default='', max_length=500)),
                ('hero_blue', models.CharField(default='', max_length=500)),
                ('hero_img', models.ImageField(default='', upload_to='images')),
                ('section_img', models.ImageField(default='', upload_to='images')),
                ('section_text', models.CharField(default='', max_length=500)),
                ('img_big', models.ImageField(default='', upload_to='images')),
                ('img_big_text', models.CharField(default='', max_length=50)),
                ('img_small1', models.ImageField(default='', upload_to='images')),
                ('img_small1_text', models.CharField(default='', max_length=50)),
                ('img_small2', models.ImageField(default='', upload_to='images')),
                ('img_small2_text', models.CharField(default='', max_length=50)),
                ('img_small3', models.ImageField(default='', upload_to='images')),
                ('img_small3_text', models.CharField(default='', max_length=50)),
                ('img_small4', models.ImageField(default='', upload_to='images')),
                ('img_small4_text', models.CharField(default='', max_length=50)),
                ('twitter_link', models.CharField(default='', max_length=500)),
                ('facebook_link', models.CharField(default='', max_length=500)),
                ('instagram_link', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
