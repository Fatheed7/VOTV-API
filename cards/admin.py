from django.contrib import admin
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('cName', 'cNumber', 'cDesc', 'cDesc_Upgrade', 'cRarity', 'cType', 'cEnergy', 'cEnergy_Upgrade')
    ordering = ['cNumber']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'keywords':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(CardAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)

admin.site.register(Card, CardAdmin)