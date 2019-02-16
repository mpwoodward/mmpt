from django.contrib import admin
from .models import Event, Location, Organization, Panelist, PanelistExpertise


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['name', 'city', 'state', ]
    search_fields = ['name', ]


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ['name', 'website', ]
    search_fields = ['name', ]


class PanelistExpertiseAdmin(admin.ModelAdmin):
    model = PanelistExpertise
    list_display = ['expertise', ]
    search_fields = ['expertise', ]


class PanelistAdmin(admin.ModelAdmin):
    model = Panelist
    list_display = ['last_name', 'first_name', 'title', 'organization', 'email', 'phone', 'contact', ]
    list_filter = ['expertise', ]
    search_fields = ['last_name', ]
    autocomplete_fields = ['expertise', 'organization', 'contact', ]


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_dt', 'name', 'location', 'attendance', 'donations', ]
    autocomplete_fields = ['film', 'location', 'panelists', ]


admin.site.register(Location, LocationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(PanelistExpertise, PanelistExpertiseAdmin)
admin.site.register(Panelist, PanelistAdmin)
admin.site.register(Event, EventAdmin)
