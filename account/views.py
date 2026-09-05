from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import AdminAuthenticationForm, ProductForm, StyleForm
from vente.models import Product, Style


class AdminLoginView(auth_views.LoginView):
	template_name = "account/login.html"
	authentication_form = AdminAuthenticationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy("account:dashboard")


@staff_member_required(login_url="account:login")
def dashboard(request):
	styles = Style.objects.all()
	products = Product.objects.select_related("style").all()
	style_form = StyleForm(prefix="style")
	product_form = ProductForm(prefix="product")

	if request.method == "POST":
		if request.POST.get("form_type") == "style":
			style_form = StyleForm(request.POST, prefix="style")
			if style_form.is_valid():
				style_form.save()
				messages.success(request, "Le style a été enregistré.")
				return redirect("account:dashboard")
		if request.POST.get("form_type") == "product":
			product_form = ProductForm(request.POST, request.FILES, prefix="product")
			if product_form.is_valid():
				product_form.save()
				messages.success(request, "L'article a été enregistré.")
				return redirect("account:dashboard")

	return render(request, "account/dashboard.html", {
		"styles": styles,
		"products": products,
		"style_count": Style.objects.count(),
		"product_count": Product.objects.count(),
		"active_style_count": Style.objects.filter(active=True).count(),
		"active_product_count": Product.objects.filter(active=True).count(),
		"style_form": style_form,
		"product_form": product_form,
	})


@staff_member_required(login_url="account:login")
def delete_style(request, pk):
	if request.method == "POST":
		style = get_object_or_404(Style, pk=pk)
		style.delete()
		messages.success(request, "Le style et ses articles ont été supprimés.")
	return redirect("account:dashboard")


@staff_member_required(login_url="account:login")
def delete_product(request, pk):
	if request.method == "POST":
		product = get_object_or_404(Product, pk=pk)
		product.delete()
		messages.success(request, "L’article a été supprimé.")
	return redirect("account:dashboard")


@staff_member_required(login_url="account:login")
def edit_style(request, pk):
	style = get_object_or_404(Style, pk=pk)
	form = StyleForm(request.POST or None, instance=style)
	if request.method == "POST" and form.is_valid():
		form.save()
		messages.success(request, "Le style a été modifié.")
		return redirect("account:dashboard")
	return render(request, "account/edit.html", {
		"form": form,
		"title": "Modifier le style",
		"description": "Mets à jour les informations de ce style.",
		"submit_label": "Enregistrer les modifications",
	})


@staff_member_required(login_url="account:login")
def edit_product(request, pk):
	product = get_object_or_404(Product, pk=pk)
	form = ProductForm(request.POST or None, request.FILES or None, instance=product)
	if request.method == "POST" and form.is_valid():
		form.save()
		messages.success(request, "L’article a été modifié.")
		return redirect("account:dashboard")
	return render(request, "account/edit.html", {
		"form": form,
		"title": "Modifier l’article",
		"description": "Mets à jour les informations de cet article.",
		"submit_label": "Enregistrer les modifications",
	})

# Create your views here.
