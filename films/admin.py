from django.conf import settings
from django.contrib import admin

from .models import Category, Director, Distributor, Film, Status, Suggestor


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['category', ]


class DirectorAdmin(admin.ModelAdmin):
    model = Director
    list_display = ['last_name', 'first_name', ]
    search_fields = ['last_name', ]


class DistributorAdmin(admin.ModelAdmin):
    model = Distributor
    list_display = ['name', 'website', ]
    search_fields = ['name', ]


class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['status', ]
    search_fields = ['status', ]

class SuggestorAdmin(admin.ModelAdmin):
    model = Suggestor
    list_display = ['last_name', 'first_name', 'email', ]
    search_fields = ['last_name', 'email', ]


class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ['title', 'release_year', 'status', ]
    search_fields = ['title', ]
    list_filter = ['status', 'categories', ]
    autocomplete_fields = ['categories', 'directors', 'distributor', 'status', 'suggested_by', ]


admin.site.site_header = settings.ADMIN_SITE_HEADER

admin.site.register(Category, CategoryAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Suggestor, SuggestorAdmin)
admin.site.register(Film, FilmAdmin)
