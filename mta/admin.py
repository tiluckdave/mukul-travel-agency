from django.contrib import admin

# Register your models here.

from .models import Data, Contact, Tour_Packages

admin.site.register(Data)
admin.site.register(Contact)
admin.site.register(Tour_Packages)
