from wagtail.core import blocks
from wagtail.images import blocks as image_blocks


class ParagraphBlock(blocks.StructBlock):
    paragraph = blocks.RichTextBlock(
        label="Paragraph",
        required=True,
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
        default="",
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Paragraph"


class ImageBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(label="Image", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Image"


class FeaturedTalkBlock(blocks.StructBlock):
    talk = blocks.PageChooserBlock(label="Talk", required=True, page_type=[])
    description = blocks.TextBlock(label="Description", required=True, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Featured talk"
