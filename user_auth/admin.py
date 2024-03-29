from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import userAuth

class CustomUserAdmin(UserAdmin):
    model = userAuth
    list_display = ['email', 'name', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ['email', 'name']
    ordering = ['email']

admin.site.register(userAuth, CustomUserAdmin)
