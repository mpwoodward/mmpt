from django.db import models


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
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name) if self.last_name and self.first_name else self.last_name
    
    class Meta:
        ordering = ['last_name', 'first_name', ]


class Film(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    trailer_url = models.URLField(blank=True, null=True, verbose_name='Trailer URL')
    website = models.URLField(blank=True, null=True, help_text="The film's website")
    synopsis = models.TextField(blank=True, null=True)
    poster_image = models.ImageField(blank=True, null=True)
    release_year = models.PositiveSmallIntegerField()
    running_time = models.PositiveSmallIntegerField(blank=True, null=True, help_text='Running time in minutes')
    directors = models.ManyToManyField(Director, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    distributor = models.ForeignKey(Distributor, blank=True, null=True, on_delete=models.SET_NULL)
    license_fees = models.PositiveSmallIntegerField(blank=True, null=True)
    licensing_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_year)
    
    class Meta:
        ordering = ['title', '-release_year', ]
