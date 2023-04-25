from django.contrib import admin

# Register your models here.
from myapp.models import Genres,Movies

admin.site.register(Genres)
admin.site.register(Movies)