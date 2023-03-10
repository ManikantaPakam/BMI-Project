from django.contrib import admin
from app1.models import BMI

# Register your models here.

class BMIAdmin(admin.ModelAdmin):
    list_display = ['user','bmi','date']

admin.site.register(BMI, BMIAdmin)