# Generated by Django 5.2 on 2025-04-05 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brigade",
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
                ("name", models.CharField(max_length=100)),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrigadeReport",
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
                ("date", models.DateField()),
                ("compiled_file", models.FileField(upload_to="brigade_reports/")),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "brigade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.brigade"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HQ",
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="brigade",
            name="hq",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.hq"
            ),
        ),
        migrations.CreateModel(
            name="Unit",
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
                ("name", models.CharField(max_length=100)),
                (
                    "brigade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.brigade"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PDFSubmission",
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
                ("date", models.DateField()),
                ("file", models.FileField(upload_to="unit_pdfs/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.unit"
                    ),
                ),
            ],
        ),
    ]
