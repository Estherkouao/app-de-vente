import os

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


ADMIN_USERNAME = "ADMIN_USERNAME"
ADMIN_EMAIL = "ADMIN_EMAIL"
ADMIN_PASSWORD = "ADMIN_PASSWORD"


def create_admin(apps, schema_editor):
    username = os.environ.get(ADMIN_USERNAME, "admin")
    email = os.environ.get(ADMIN_EMAIL, "")
    password = os.environ.get(ADMIN_PASSWORD)

    if not password:
        raise RuntimeError(
            "ADMIN_PASSWORD doit être défini avant d'exécuter les migrations. "
            "Exemple : ADMIN_PASSWORD='mot-de-passe-fort' python manage.py migrate"
        )

    app_label, model_name = settings.AUTH_USER_MODEL.split(".")
    user_model = apps.get_model(app_label, model_name)
    user, created = user_model.objects.get_or_create(
        username=username,
        defaults={
            "email": email,
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )

    if created:
        user.password = make_password(password)
        user.save(update_fields=["password"])
    else:
        changed = False
        for field, value in (
            ("email", email),
            ("is_staff", True),
            ("is_superuser", True),
            ("is_active", True),
        ):
            if getattr(user, field) != value:
                setattr(user, field, value)
                changed = True
        if changed:
            user.save(update_fields=["email", "is_staff", "is_superuser", "is_active"])


def remove_admin(apps, schema_editor):
    # Never delete an administrator when this data migration is reversed.
    pass


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vente", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_admin, remove_admin),
    ]
