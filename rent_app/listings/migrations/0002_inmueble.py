# Generated by Django 5.1.3 on 2024-11-15 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Inmueble",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_inmueble",
                    models.CharField(
                        choices=[
                            ("Departamento", "Departamento"),
                            ("Casa", "Casa"),
                            ("Cuarto", "Cuarto"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "distancia",
                    models.CharField(
                        choices=[
                            ("0-5 km", "0-5 km"),
                            ("5-10 km", "5-10 km"),
                            ("10-15 km", "10-15 km"),
                        ],
                        max_length=50,
                    ),
                ),
                ("direccion", models.CharField(max_length=255)),
                ("codigo_postal", models.CharField(max_length=10)),
                ("descripcion", models.TextField()),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                ("numero_contacto", models.CharField(max_length=15)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="inmuebles/"),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
