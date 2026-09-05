from django import forms
from django.contrib.auth.forms import AuthenticationForm

from vente.models import Product, Style


class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = ["name", "icon", "color", "order", "active"]
        labels = {
            "name": "Nom du style",
            "icon": "Icône",
            "color": "Couleur",
            "order": "Ordre d’affichage",
            "active": "Style actif",
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "style",
            "name",
            "category",
            "price",
            "old_price",
            "discount",
            "tone",
            "image",
            "active",
        ]
        labels = {
            "style": "Style",
            "name": "Nom de l’article",
            "category": "Catégorie",
            "price": "Prix actuel",
            "old_price": "Ancien prix",
            "discount": "Réduction",
            "tone": "Teinte de l’image",
            "image": "Image de l’article",
            "active": "Article actif",
        }


class AdminAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nom d’utilisateur")
    password = forms.CharField(label="Mot de passe", strip=False, widget=forms.PasswordInput)
