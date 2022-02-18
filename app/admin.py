from django.contrib import admin

from app.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_fish', 'timestamp', 'photo')
    list_display_links = ('id', 'name_of_fish')
    list_filter = ('timestamp',)
    search_fields = ('name_of_fish', 'photo')
    list_per_page = 25


admin.site.register(Record, RecordAdmin)
