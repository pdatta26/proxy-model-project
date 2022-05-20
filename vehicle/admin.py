from django.contrib import admin
from .models import *


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('pk', 'model', 'brand', 'wheel')
    list_filter = ('model', 'brand', 'wheel')
    list_editable = ('model', 'brand', 'wheel')
    list_display_links = ('pk',)
    list_per_page = 2


class HondaAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('pk', 'model', 'brand', 'wheel')
    list_filter = ('model', 'brand', 'wheel')
    list_editable = ('model', 'brand', 'wheel')
    list_display_links = ('pk',)
    list_per_page = 2


class PrivetCarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('pk', 'model', 'brand', 'wheel')
    list_filter = ('model', 'brand', 'wheel')
    list_editable = ('model', 'brand', 'wheel')
    list_display_links = ('pk',)
    list_per_page = 2


admin.site.register(Car, CarAdmin)
admin.site.register(Honda, HondaAdmin)
admin.site.register(PrivetCar, PrivetCarAdmin)
