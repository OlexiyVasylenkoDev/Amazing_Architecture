from django.contrib import admin

from architectors.models import Architector, Company

# Register your models here.
admin.site.register([Architector, Company])