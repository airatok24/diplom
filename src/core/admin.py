from django.contrib import admin

from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'last_name', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'last_name', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permissions',
            {'fields':('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )
