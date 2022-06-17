# Generated by Django 3.2.11 on 2022-06-17 09:43

import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Start date")),
                ("end_date", models.DateField(verbose_name="End date")),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "paragraph",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "paragraph",
                                            wagtail.core.blocks.RichTextBlock(
                                                default="",
                                                features=[
                                                    "bold",
                                                    "italic",
                                                    "h2",
                                                    "h3",
                                                    "h4",
                                                    "h5",
                                                    "ol",
                                                    "ul",
                                                    "link",
                                                    "document",
                                                    "embed",
                                                ],
                                                label="Paragraph",
                                                required=True,
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "image",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                label="Image", required=True
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "featuredtalk",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "talk",
                                            wagtail.core.blocks.PageChooserBlock(
                                                label="Talk",
                                                page_type=[],
                                                required=True,
                                            ),
                                        ),
                                        (
                                            "description",
                                            wagtail.core.blocks.TextBlock(
                                                default="",
                                                label="Description",
                                                required=True,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                        default="",
                        verbose_name="Body",
                    ),
                ),
            ],
            options={
                "verbose_name": "Event",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Homepage",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="TalkPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "abstract",
                    wagtail.core.fields.RichTextField(
                        blank=True, default="", verbose_name="Abstract"
                    ),
                ),
            ],
            options={
                "verbose_name": "Talk",
            },
            bases=("wagtailcore.page",),
        ),
    ]
