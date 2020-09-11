from django.contrib import admin
from auth_token.models import AuthToken


# Register your models here.


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):

    def is_expired(self, obj):
        """检测 token 是否过期"""
        return obj.is_expired

    list_display = ['name', 'token', 'owner', 'status', 'is_expired', 'start', 'end']
    list_filter = ['status']
    search_fields = ['name', 'token', 'owner_username']
    is_expired.short_description = '是否过期'
    fieldsets = [
        ('基本信息', {'classes': ['grp-collapse grp-open'], 'fields': ['name', 'token', 'owner']}),
        ('时间管理', {'classes': ['grp-collapse grp-open'], 'fields': ['start', 'end']}),
        ('状态管理', {'classes': ['grp-collapse grp-open'], 'fields': ['status']}),
    ]
