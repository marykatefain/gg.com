from django.db import models

from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel
)


class BlogIndexPage(Page):

    subpage_types = ['BlogPostPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['blog_pages'] = self.get_children().live().order_by('-first_published_at').specific
        return context


class BlogPostPage(Page):
    headline = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    listing_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('subtitle'),
        FieldPanel('body'),
        ImageChooserPanel('listing_image'),
    ]

    parent_page_types = ['BlogIndexPage']
