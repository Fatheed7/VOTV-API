from django.contrib import admin
from .models import Keywords
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'kNumber')
    ordering = ['kNumber']
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'related_keywords':
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(KeywordsAdmin, self).formfield_for_manytomany(
            db_field, request, **kwargs)

admin.site.register(Keywords, KeywordsAdmin)
