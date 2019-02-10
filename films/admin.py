from django.contrib import admin
from .models import Category, Director, Distributor, Film


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['name', ]


class DirectorAdmin(admin.ModelAdmin):
    model = Director
    list_display = ['last_name', 'first_name', ]
    search_fields = ['last_name', ]


class DistributorAdmin(admin.ModelAdmin):
    model = Distributor
    list_display = ['name', 'website', ]
    search_fields = ['name', ]


class FilmAdmin(admin.ModelAdmin):
    model = Film
    list_display = ['title', 'release_year', ]
    autocomplete_fields = ['categories', 'directors', 'distributor', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Film, FilmAdmin)
