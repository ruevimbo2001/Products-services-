from django.contrib import admin
from .models import HairbraidingService

admin.site.register('HairbraidingService')
@admin.register(HairbraidingService)
class HairbraidingServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'duration')
    search_fields = ('name',)
