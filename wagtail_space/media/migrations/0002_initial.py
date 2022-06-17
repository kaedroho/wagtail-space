# Generated by Django 3.2.11 on 2022-04-04 15:17

import django.db.models.deletion
import taggit.managers
import wagtail.core.models.collections
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("media", "0001_initial"),
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="customimage",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="collection",
            field=models.ForeignKey(
                default=wagtail.core.models.collections.get_root_collection_id,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.collection",
                verbose_name="collection",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text=None,
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="customrendition",
            unique_together={("image", "filter_spec", "focal_point_key")},
        ),
    ]