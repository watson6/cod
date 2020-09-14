from django.contrib import admin
from silence.models import Silence


# Register your models here.


@admin.register(Silence)
class SilenceAdmin(admin.ModelAdmin):
    list_display = ['owner', 'project', 'duration', 'ignore_type', 'created', 'modified']
    list_filter = ['project', 'ignore_type']
    search_fields = ['owner__username', 'project__name']
    fieldsets = [
        ('基本信息', {'classes': ['grp-collapse grp-open'], 'fields': ['project', 'duration', 'owner', 'filter_args']}),
        ('选择开关', {'classes': ['grp-collapse grp-open'], 'fields': ['ignore_type']}),
    ]
