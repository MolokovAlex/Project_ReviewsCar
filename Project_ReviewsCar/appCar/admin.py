from django.contrib import admin

from .models import *

class CountryInAdminPage(admin.ModelAdmin):
    list_display = ('id_country', 'country_name')

class ManufInAdminPage(admin.ModelAdmin):
    list_display = ('id_manuf', 'manuf_name', 'manuf_country')

class CarInAdminPage(admin.ModelAdmin):
    list_display = ('id_car', 'car_name', 'car_manuf', 'car_date_start_manuf', 'car_date_end_manuf')

class CommentInAdminPage(admin.ModelAdmin):
    list_display = ('id_comment', 'comment_email', 'comment_car', 'comment_date_publ', 'comment_text_comment')    

admin.site.register(Country, CountryInAdminPage)
admin.site.register(Manuf, ManufInAdminPage)
admin.site.register(Car, CarInAdminPage)
admin.site.register(Comment, CommentInAdminPage)