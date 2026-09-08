from django.shortcuts import render

from .models import Product, Style


DEFAULT_PRODUCTS = [
	{"name": "Casquette Solaire", "category": "Mode", "price": "12 500 FCFA", "old_price": "18 000 FCFA", "discount": "-30%", "tone": "coral"},
	{"name": "Sac Urbain", "category": "Lifestyle", "price": "18 000 FCFA", "old_price": "25 000 FCFA", "discount": "-28%", "tone": "blue"},
	{"name": "Lunettes Éclat", "category": "Beauté", "price": "9 500 FCFA", "old_price": "14 000 FCFA", "discount": "-32%", "tone": "gold"},
	{"name": "Écouteurs Move", "category": "Tech", "price": "22 000 FCFA", "old_price": "30 000 FCFA", "discount": "-26%", "tone": "green"},
]

DEFAULT_STYLES = [
	{"name": "Mode", "icon": "✦", "color": "coral"},
	{"name": "Maison", "icon": "⌂", "color": "blue"},
	{"name": "Beauté", "icon": "◌", "color": "gold"},
	{"name": "Tech", "icon": "⌁", "color": "ink"},
	{"name": "Lifestyle", "icon": "↗", "color": "green"},
	{"name": "Idées cadeaux", "icon": "♡", "color": "pink"},
]


def home(request):
	styles = list(Style.objects.filter(active=True))
	products = list(Product.objects.filter(active=True).select_related("style"))
	return render(request, "home.html", {
		"styles": styles or DEFAULT_STYLES,
		"products": products or DEFAULT_PRODUCTS,
		"whatsapp_number": "+2250153183316",
		"active_filter": request.GET.get("style", ""),
	})


def filter_products(request):
	style_name = request.GET.get("style", "")
	styles = list(Style.objects.filter(active=True))
	if style_name:
		products = list(Product.objects.filter(active=True, style__name=style_name).select_related("style"))
	else:
		products = list(Product.objects.filter(active=True).select_related("style"))
	return render(request, "home.html", {
		"styles": styles or DEFAULT_STYLES,
		"products": products or DEFAULT_PRODUCTS,
		"whatsapp_number": "+2250700000000",
		"active_filter": style_name,
	})
