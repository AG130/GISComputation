from django.contrib import admin

# Register your models here.

from first_welcome import models
admin.site.register(models.User)
