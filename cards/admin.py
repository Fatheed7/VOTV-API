from django.contrib import admin

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gameClass', 'type', 'rarity',)
    ordering = ['id']


admin.site.register(Card, CardAdmin)