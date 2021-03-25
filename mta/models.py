from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.


class Data(models.Model):
    data_id = models.AutoField
    data_name = models.CharField(max_length=50, default="main")

    logo = models.ImageField(upload_to="images", default="")
    favicon = models.ImageField(upload_to="images", default="")

    phone_no = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=50, default="")
    address_l1 = models.CharField(max_length=50, default="")
    address_l2 = models.CharField(max_length=50, default="")
    address_l3 = models.CharField(max_length=50, default="")
    address_l4 = models.CharField(max_length=50, default="")
    address_l5 = models.CharField(max_length=50, default="")
    email_id = models.EmailField(default="")

    hero_pink = models.CharField(max_length=500, default="")
    hero_black = models.CharField(max_length=500, default="")
    hero_grey_l1 = models.CharField(max_length=500, default="")
    hero_grey_l2 = models.CharField(max_length=500, default="")
    hero_grey_l3 = models.CharField(max_length=500, default="")
    hero_grey_l4 = models.CharField(max_length=500, default="")
    hero_grey_l5 = models.CharField(max_length=500, default="")
    hero_blue = models.CharField(max_length=500, default="")
    hero_img = models.ImageField(upload_to="images", default="")

    section_img = models.ImageField(upload_to="images", default="")
    section_text = models.CharField(max_length=500, default="")

    twitter_link = models.CharField(max_length=500, default="")
    facebook_link = models.CharField(max_length=500, default="")
    instagram_link = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.data_name

class Tour_Packages(models.Model):
    sno = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images", default="")
    name = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email_id = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=13, default="")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.first_name + ' - ' + self.email_id
