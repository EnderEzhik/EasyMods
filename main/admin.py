from django.contrib import admin
from .models import Mod, Category, Version


admin.site.register(Mod)
admin.site.register(Category)
admin.site.register(Version)