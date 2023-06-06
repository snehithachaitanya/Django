from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(horrorDB)
admin.site.register(newsDB)
admin.site.register(pompletDB)
admin.site.register(instaDB)
admin.site.register(actionDB)
admin.site.register(DevDB)