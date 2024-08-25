from django.contrib import admin
from .models import Adopcion

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'adoptante', 'fecha_adopcion')
    search_fields = ('mascota__nombre', 'adoptante')
    list_filter = ('fecha_adopcion',)
    date_hierarchy = 'fecha_adopcion'
