from wagtail.core import blocks


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(label="Quote", required=True, default="")
    attribution = blocks.TextBlock(label="Attribution", required=False, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Quote"
