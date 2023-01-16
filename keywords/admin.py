from django.contrib import admin
from .models import Keywords

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'kNumber')
    ordering = ['kNumber']

admin.site.register(Keywords, KeywordsAdmin)
