# Generated by Django 2.1.5 on 2019-02-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_suggestor_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='suggested_by',
        ),
        migrations.AddField(
            model_name='film',
            name='suggested_by',
            field=models.ManyToManyField(blank=True, to='films.Suggestor'),
        ),
    ]
