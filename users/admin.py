from django.contrib import admin

from users.models import User

'''админка для пользователей'''
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'phone', 'city', 'first_name', 'last_name', 'is_active',)
    list_filter = ('city',)