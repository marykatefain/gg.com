# Generated by Django 2.0.9 on 2018-10-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='tagline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
