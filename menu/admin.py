
from django.contrib import admin
from .models import Category, MenuItem, Reservation, ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at', 'message')
	search_fields = ('name', 'email', 'message')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'price')
	list_filter = ('category',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'date', 'time', 'guests', 'message')
	search_fields = ('name', 'email', 'phone', 'message')
