from django.db import models

from ckeditor.fields import RichTextField
from localflavor.us.models import USStateField, USZipCodeField

from films.models import Film


class Location(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = USStateField()
    postal_code = USZipCodeField()
    notes = RichTextField(blank=True, null=True, help_text='Any special instructions related to this location')

    def __str__(self):
        return '{} - {}, {}'.format(self.name, self.city, self.state)
    
    class Meta:
        ordering = ['name', ]
 

class Organization(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    website = models.URLField(blank=True, null=True)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name', ]


class Panelist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(blank=True, null=True, unique=True, db_index=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
    
    class Meta:
        ordering = ['last_name', 'first_name', ]
    

class Event(models.Model):
    name = models.CharField(max_length=500, db_index=True)
    film = models.ForeignKey(Film, db_index=True, on_delete=models.CASCADE)
    event_dt = models.DateTimeField(db_index=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    details = RichTextField(blank=True, null=True)
    panelists = models.ManyToManyField(Panelist, blank=True)
    sponsors = RichTextField(blank=True, null=True)
    more_info_url = models.URLField(blank=True, null=True, verbose_name='URL for More Info')
    facebook_event_url = models.URLField(blank=True, null=True, verbose_name='Facebook Event URL')
    attendance = models.PositiveSmallIntegerField(blank=True, null=True, db_index=True)
    donations = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.event_dt, self.name)
    
    class Meta:
        ordering = ['-event_dt', ]
