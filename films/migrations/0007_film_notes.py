# Generated by Django 2.1.5 on 2019-02-10 13:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_auto_20190210_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Any relevant discussion notes or concerns about the film', null=True),
        ),
    ]
