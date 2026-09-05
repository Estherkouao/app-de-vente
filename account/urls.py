from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import AdminLoginView, dashboard
from .views import AdminLoginView, dashboard, delete_product, delete_style, edit_product, edit_style

app_name = "account"

urlpatterns = [
    path("login/", AdminLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("styles/<int:pk>/supprimer/", delete_style, name="delete_style"),
    path("articles/<int:pk>/supprimer/", delete_product, name="delete_product"),
    path("styles/<int:pk>/modifier/", edit_style, name="edit_style"),
    path("articles/<int:pk>/modifier/", edit_product, name="edit_product"),
]
