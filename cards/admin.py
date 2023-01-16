from django.contrib import admin

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('cName', 'cNumber', 'cDesc', 'cDesc_Upgrade', 'cRarity', 'cType', 'cEnergy', 'cEnergy_Upgrade')
    ordering = ['cNumber']


admin.site.register(Card, CardAdmin)