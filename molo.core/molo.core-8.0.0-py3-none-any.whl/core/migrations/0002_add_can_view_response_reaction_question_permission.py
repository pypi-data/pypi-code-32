# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import molo.core.blocks
import molo.core.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0077_molo_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reactionquestionresponse',
            options={'permissions': (('can_view_response', 'Can view Response'),)},
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', molo.core.blocks.MarkDownBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('numbered_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('page', wagtail.core.blocks.PageChooserBlock()), ('media', molo.core.models.MoloMediaBlock(icon='media'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='commenting_state',
            field=models.CharField(blank=True, choices=[('O', 'Open'), ('C', 'Closed'), ('D', 'Disabled'), ('T', 'Timestamped')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='social_media_description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='social_media_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='social_media_title',
            field=models.TextField(blank=True, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='bannerpage',
            name='external_link',
            field=models.TextField(blank=True, help_text='External link which a banner will link to. eg https://www.google.co.za/', null=True),
        ),
        migrations.AlterField(
            model_name='languagepage',
            name='commenting_state',
            field=models.CharField(blank=True, choices=[('O', 'Open'), ('C', 'Closed'), ('D', 'Disabled'), ('T', 'Timestamped')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='sectionindexpage',
            name='commenting_state',
            field=models.CharField(blank=True, choices=[('O', 'Open'), ('C', 'Closed'), ('D', 'Disabled'), ('T', 'Timestamped')], default='O', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='commenting_state',
            field=models.CharField(blank=True, choices=[('O', 'Open'), ('C', 'Closed'), ('D', 'Disabled'), ('T', 'Timestamped')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='content_rotation_end_date',
            field=models.DateTimeField(blank=True, help_text='The date rotation will end', null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='content_rotation_start_date',
            field=models.DateTimeField(blank=True, help_text='The date rotation will begin', null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='enable_next_section',
            field=models.BooleanField(default=False, help_text="Activate up next section underneath articles in this section will appear with the heading and subheading of that article. The text will say 'next' in order to make the user feel like it's fresh content.", verbose_name='Activate up next section underneath articles'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='enable_recommended_section',
            field=models.BooleanField(default=False, help_text="Underneath the area for 'next articles' recommended articles will appear, with the image + heading + subheading", verbose_name='Activate recommended section underneath articles'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='extra_style_hints',
            field=models.TextField(blank=True, default='', help_text='Styling options that can be applied to this section and all its descendants', null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='friday_rotation',
            field=models.BooleanField(default=False, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='monday_rotation',
            field=models.BooleanField(default=False, verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='saturday_rotation',
            field=models.BooleanField(default=False, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='sunday_rotation',
            field=models.BooleanField(default=False, verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='thursday_rotation',
            field=models.BooleanField(default=False, verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='time',
            field=wagtail.core.fields.StreamField((('time', wagtail.core.blocks.TimeBlock(required=False)),), blank=True, help_text='The time/s content will be rotated', null=True),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='tuesday_rotation',
            field=models.BooleanField(default=False, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='wednesday_rotation',
            field=models.BooleanField(default=False, verbose_name='Wednesday'),
        ),
        migrations.AlterField(
            model_name='sitelanguage',
            name='locale',
            field=models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zu', 'Zulu'), ('xh', 'Xhosa'), ('st', 'Sotho'), ('ve', 'Venda'), ('tn', 'Tswana'), ('ts', 'Tsonga'), ('ss', 'Swati'), ('nr', 'Ndebele')], help_text='Site language', max_length=255, verbose_name='language name'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='content_rotation_end_date',
            field=models.DateTimeField(blank=True, help_text='The date rotation will end', null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='content_rotation_start_date',
            field=models.DateTimeField(blank=True, help_text='The date rotation will begin', null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='enable_clickable_tags',
            field=models.BooleanField(default=False, verbose_name='Display tags on Front-end'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='enable_service_directory',
            field=models.BooleanField(default=False, verbose_name='Enable service directory'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='enable_tag_navigation',
            field=models.BooleanField(default=False, help_text='Enable tag navigation. When this is true, the clickable tag functionality will be overriden'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='facebook_sharing',
            field=models.BooleanField(default=False, help_text='Enable this field to allow for sharing to Facebook.', verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='friday_rotation',
            field=models.BooleanField(default=False, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='monday_rotation',
            field=models.BooleanField(default=False, verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='saturday_rotation',
            field=models.BooleanField(default=False, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='show_only_translated_pages',
            field=models.BooleanField(default=False, help_text='When selecting this option, untranslated pages will not be visible to the front end user when they viewing a child language of the site'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='social_media_links_on_footer_page',
            field=wagtail.core.fields.StreamField((('social_media_site', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='sunday_rotation',
            field=models.BooleanField(default=False, verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='thursday_rotation',
            field=models.BooleanField(default=False, verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='time',
            field=wagtail.core.fields.StreamField((('time', wagtail.core.blocks.TimeBlock(required=False)),), blank=True, help_text='The time/s content will be rotated', null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='tuesday_rotation',
            field=models.BooleanField(default=False, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='twitter_sharing',
            field=models.BooleanField(default=False, help_text='Enable this field to allow for sharing to Twitter.', verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='wednesday_rotation',
            field=models.BooleanField(default=False, verbose_name='Wednesday'),
        ),
    ]
