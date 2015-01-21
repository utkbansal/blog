from django.contrib import admin
from .models import Entry
from django_summernote.admin import SummernoteModelAdmin


class EntryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Entry, EntryAdmin)