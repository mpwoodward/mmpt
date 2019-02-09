from django.contrib import admin
from .models import Category, Director, Distributor, Film


class DirectorAdmin(admin.ModelAdmin):
    model = Director
    list_display = ['last_name', 'first_name', ]


class DistributorAdmin(admin.ModelAdmin):
    model = Distributor
    list_display = ['name', 'website', ]


class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ['title', 'release_year', ]


admin.site.register(Category)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Film, FilmAdmin)
