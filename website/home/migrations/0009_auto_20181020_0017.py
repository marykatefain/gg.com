# Generated by Django 2.0.9 on 2018-10-20 00:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20181012_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='portal_cards',
            field=wagtail.core.fields.StreamField([('portal_card', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock())), ('image', wagtail.images.blocks.ImageChooserBlock()), ('headline', wagtail.core.blocks.CharBlock(required=True)), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))], blank=True, null=True),
        ),
    ]
