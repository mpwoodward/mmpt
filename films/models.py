from django.db import models

from ckeditor.fields import RichTextField
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class Category(models.Model):
    category = models.CharField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['category', ]
        verbose_name_plural = 'Categories'
    

class Distributor(models.Model):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    website = models.URLField(blank=True, null=True)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name if self.first_name and self.last_name else self.last_name
    
    class Meta:
        ordering = ['last_name', 'first_name', ]
        unique_together = ('last_name', 'first_name')


class Suggestor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    class Meta:
        ordering = ['last_name', 'first_name', ]


class Status(models.Model):
    status = models.CharField(max_length=100, unique=True, db_index=True)
    ordering = models.PositiveSmallIntegerField(unique=True, db_index=True)

    def __str__(self):
        return self.status
    
    class Meta:
        ordering = ['ordering', ]


class Film(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    trailer_url = models.URLField(blank=True, null=True, verbose_name='Trailer URL')
    website = models.URLField(blank=True, null=True, help_text="The film's website")
    synopsis = RichTextField(blank=True, null=True)
    poster_image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)
    release_year = models.PositiveSmallIntegerField()
    running_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text='Running time in minutes')
    directors = models.ManyToManyField(Director, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.SET_NULL)
    suggested_by = models.ManyToManyField(Suggestor, blank=True)
    notes = RichTextField(blank=True, null=True, help_text='Any relevant discussion notes or concerns about the film')
    distributor = models.ForeignKey(Distributor, blank=True, null=True, on_delete=models.SET_NULL)
    license_fees = models.PositiveSmallIntegerField(blank=True, null=True)
    licensing_notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_year)
    
    class Meta:
        ordering = ['title', '-release_year', ]
        unique_together = ('title', 'release_year')
