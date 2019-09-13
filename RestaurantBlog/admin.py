from django.contrib import admin

from .models import Restaurant,Dish,Review

class RestaurantList(admin.ModelAdmin):
    list_display = ( 'restaurant_name', 'email', 'phone_number' )
    list_filter = ( 'restaurant_name', 'email')
    search_fields = ('restaurant_name', )
    ordering = ['restaurant_name']

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)