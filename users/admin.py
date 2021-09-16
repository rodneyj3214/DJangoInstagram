from django.contrib import admin

from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number',)
    search_fields = ('user__email', 'user__first_name', 'user__username', 'user__last_name')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff',)
