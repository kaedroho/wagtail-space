from django.db import models
from wagtail import images
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Speaker(index.Indexed, models.Model):
    name = models.TextField(verbose_name="Name", default="")
    photo = models.ForeignKey(
        to=images.get_image_model_string(),
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Photo",
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel("name"),
        image_edit_handlers.ImageChooserPanel("photo"),
    ]

    search_fields = [
        index.SearchField("name"),
        index.FilterField("name"),
        index.FilterField("photo"),
    ]

    def __str__(self):
        if self.name:
            return self.name
        return super().__str__()

    preview_modes = []

    class Meta:
        verbose_name = "Speaker"
