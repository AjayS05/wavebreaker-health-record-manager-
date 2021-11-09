from django.contrib import admin
from .models import organization, department,recordss, cities, hospital, oxygen, vaccine
# Register your models here.
admin.site.register(organization)
admin.site.register(department)
admin.site.register(recordss)
admin.site.register(cities)
admin.site.register(hospital)
admin.site.register(oxygen)
admin.site.register(vaccine)
