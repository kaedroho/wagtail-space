# Generated by Django 3.2.11 on 2022-06-17 09:43

import django.db.models.deletion
import wagtail.search.index
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("media", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speaker",
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
                ("name", models.TextField(default="", verbose_name="Name")),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="media.customimage",
                        verbose_name="Photo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Speaker",
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
