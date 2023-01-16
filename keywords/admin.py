from django.contrib import admin
from .models import Keywords

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id')
    ordering = ['id']

admin.site.register(Keywords, KeywordsAdmin)
