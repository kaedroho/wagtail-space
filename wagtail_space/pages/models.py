from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.snippets import edit_handlers as snippet_edit_handlers

from wagtail_space.pages import blocks as pages_blocks


class TalkPage(Page):
    speaker = models.ForeignKey(
        to="snippets.Speaker",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Speaker",
        blank=True,
        null=True,
    )
    abstract = RichTextField(
        verbose_name="Abstract",
        blank=True,
        features=["bold", "italic", "ol", "ul", "link", "image", "document", "embed"],
        default="",
    )

    content_panels = Page.content_panels + [
        snippet_edit_handlers.SnippetChooserPanel("speaker"),
        FieldPanel("abstract"),
    ]

    search_fields = Page.search_fields + [
        index.FilterField("speaker"),
        index.SearchField("abstract"),
        index.FilterField("abstract"),
    ]

    subpage_types = []
    parent_page_types = [
        "pages.EventPage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Talk"


class EventPage(Page):
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    body = StreamField(
        block_types=[
            ("paragraph", pages_blocks.ParagraphBlock()),
            ("image", pages_blocks.ImageBlock()),
            ("featuredtalk", pages_blocks.FeaturedTalkBlock()),
        ],
        default="",
        verbose_name="Body",
        blank=True,
    )

    dates_panels = [
        FieldPanel("start_date"),
        FieldPanel("end_date"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Dates", children=dates_panels),
        StreamFieldPanel("body"),
    ]

    subpage_types = [
        "pages.TalkPage",
    ]
    parent_page_types = [
        "pages.HomePage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Event"


class HomePage(Page):

    subpage_types = [
        "pages.EventPage",
    ]
    parent_page_types = [
        "wagtailcore.Page",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Homepage"
