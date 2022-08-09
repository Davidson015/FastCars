from django.contrib import admin
from app.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# Exporting data to CSV file
# Brand model
class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = [
    'name',
  ]

# Vehicle model
class VehicleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = [
    'model',
    'make',
    'image',
    'description',
    'price',
    'year',
  ]

# Booking model
class BookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = [
    'pick_up_location',
    'pick_up_date',
    'pick_up_time',
    'drop_off_location',
    'drop_off_date',
    'drop_off_time',
    'get_chaffeur_driven',
    'vehicle',
  ]

# Testimonial model
class TestimonialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = [
    'review',
    'client_image',
    'client_name',
    'rating',
  ]

# Registering the models to the admin site
admin.site.register(Brand, BrandAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Testimonial, TestimonialAdmin)