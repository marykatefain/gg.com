from django.db import models

from wagtail.core import blocks

from wagtail.core.models import Page

from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel

from website.blocks import ImageInfoSection, PortfolioCard


class PortfolioPage(Page):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    portfolio_cards = StreamField(
        [
            ('portfolio_cards', PortfolioCard())
        ]
    )
    body = StreamField(
        [
            ('image_info_section', ImageInfoSection())
        ],
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('subtitle'),
        StreamFieldPanel('portfolio_cards'),
        StreamFieldPanel('body'),
    ]
