from        django.urls import path
from . import views

app_name = "vente"

urlpatterns = [
	
    path("", views.home, name="home"),
	path("filter/", views.filter_products, name="filter_products"),
]


