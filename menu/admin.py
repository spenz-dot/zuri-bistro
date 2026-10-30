from django.contrib import admin
from .models import Category, MenuItem, Reservation


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available")
    list_filter = ("category", "available")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "date", "time", "guests")
    ordering = ("date", "time")


admin.site.register(Category)
