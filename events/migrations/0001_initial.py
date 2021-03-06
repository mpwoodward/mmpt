# Generated by Django 2.1.5 on 2019-02-09 21:39

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=500)),
                ('event_dt', models.DateTimeField(db_index=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('sponsors', models.TextField(blank=True, null=True)),
                ('more_info_url', models.URLField(blank=True, null=True, verbose_name='URL for More Info')),
                ('facebook_event_url', models.URLField(blank=True, null=True, verbose_name='Facebook Event URL')),
                ('attendance', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('donations', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Film')),
            ],
            options={
                'ordering': ['-event_dt'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('postal_code', localflavor.us.models.USZipCodeField(max_length=10)),
                ('notes', models.TextField(blank=True, help_text='Any special instructions related to this location', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('website', models.URLField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(db_index=True, max_length=100)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Organization')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='panelists',
            field=models.ManyToManyField(blank=True, to='events.Panelist'),
        ),
    ]
