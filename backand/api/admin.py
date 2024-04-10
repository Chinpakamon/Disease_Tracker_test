from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'password')
    search_fields = ('username',)
    list_filter = ('email',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
