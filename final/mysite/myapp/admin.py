from django.contrib import admin
from myapp.models import DataList
# Register your models here.

@admin.register(DataList)
class DataListAdmin(admin.ModelAdmin):
    pass