from django.contrib import admin

# Register your models here.

from .models import Grupos,Grupo

admin.site.register(Grupos)
admin.site.register(Grupo)
