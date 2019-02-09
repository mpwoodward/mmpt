from django.contrib import admin
from .models import Location, Organization, Panelist, Event


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['name', 'city', 'state', ]


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ['name', 'website', ]


class PanelistAdmin(admin.ModelAdmin):
    model = Panelist
    list_display = ['last_name', 'first_name', 'title', 'organization', 'email', 'phone', ]


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_dt', 'name', 'location', 'attendance', 'donations', ]


admin.site.register(Location, LocationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Panelist, PanelistAdmin)
admin.site.register(Event, EventAdmin)
