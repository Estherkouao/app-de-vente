from django.db import models


class Style(models.Model):
	name = models.CharField(max_length=80, unique=True)
	icon = models.CharField(max_length=10, default="✦")
	color = models.CharField(max_length=30, default="coral")
	order = models.PositiveIntegerField(default=0)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ["order", "name"]

	def __str__(self):
		return self.name


class Product(models.Model):
	style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name="products")
	name = models.CharField(max_length=120)
	category = models.CharField(max_length=80, blank=True)
	price = models.CharField(max_length=40)
	old_price = models.CharField(max_length=40, blank=True)
	discount = models.CharField(max_length=20, blank=True)
	tone = models.CharField(max_length=30, default="coral")
	image = models.ImageField(upload_to="products/", blank=True)
	active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return self.name
