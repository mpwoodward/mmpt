# Generated by Django 2.1.5 on 2019-02-10 01:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Any special instructions related to this location', null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panelist',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
