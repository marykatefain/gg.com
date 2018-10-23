from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel


@register_setting
class SiteSettings(BaseSetting):
    tagline = models.CharField(max_length=200, blank=True, null=True)

    panels = [
        FieldPanel('tagline'),
    ]
