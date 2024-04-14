from django.contrib import admin
from .models import File


class ArrivedDepartedFilter(admin.SimpleListFilter):
    title = 'Arrival Status'
    parameter_name = 'arrival_status'

    def lookups(self, request, model_admin):
        return (
            ('arrived', 'Arrived'),
            ('departed', 'Departed'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'arrived':
            return queryset.filter(arrived=True)
        elif self.value() == 'departed':
            return queryset.filter(arrived=False)


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'filename', 'uploaded_at', 'user', 'arrived')
    list_filter = (ArrivedDepartedFilter,)
    search_fields = ['title', 'user__username']


admin.site.register(File, FileAdmin)
