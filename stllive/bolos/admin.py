from django.contrib import admin

# Register your models here.
from .models import Bolo, Sabor
admin.site.register(Bolo)
admin.site.register(Sabor)