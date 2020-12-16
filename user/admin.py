from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "nick_name", "username", "email")
    list_display_links = ("nick_name", )
    search_fields = ("nick_name", )