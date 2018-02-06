from django.contrib import admin
from .models import Barcamp, Speaker, Talk

# Register your models here.
admin.site.register(Barcamp)
admin.site.register(Speaker)
admin.site.register(Talk)
