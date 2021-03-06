from django.contrib import admin
from event.models import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'host', 'level', 'grade', 'converge', 'status', 'is_removed', 'created', 'modified']
    list_filter = ['status', 'is_removed']
    search_fields = ['name', 'project_name']
    filter_horizontal = ['messages', 'receivers']
    fieldsets = [
        ('基本信息', {'classes': ['grp-collapse grp-open'], 'fields': ['name', 'project', 'host', 'level', 'grade', 'converge', 'owner']}),
        ('人员管理', {'classes': ['grp-collapse grp-open'], 'fields': ['messages', 'receivers']}),
        ('标签管理', {'classes': ['grp-collapse grp-open'], 'fields': ['tags']}),
        ('标记删除', {'classes': ['grp-collapse grp-open'], 'fields': ['is_removed']}),
    ]
