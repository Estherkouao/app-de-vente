from django.contrib import admin

from .models import Product, Style


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
	list_display = ("name", "color", "order", "active")
	list_editable = ("color", "order", "active")
	search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "style", "price", "active", "created_at")
	list_filter = ("style", "active")
	search_fields = ("name", "category")
	list_editable = ("active",)
