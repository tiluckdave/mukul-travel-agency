# Generated by Django 3.1.4 on 2020-12-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='facebook_link',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='hero_black',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='hero_blue',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='hero_grey',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='home',
            name='hero_img',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='hero_pink',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='home_name',
            field=models.CharField(default='main', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='img_big',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='img_big_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small1',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small1_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small2',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small2_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small3',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small3_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small4',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='img_small4_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='instagram_link',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='phone_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='home',
            name='section_img',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='home',
            name='section_text',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='home',
            name='twitter_link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
