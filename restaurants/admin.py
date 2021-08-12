from django.contrib import admin
from restaurants.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    fieldsets = (("Restaurant Info", {"fields": ("name",)}),)


admin.site.register(Restaurant, RestaurantAdmin)
