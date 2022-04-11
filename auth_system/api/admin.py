from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_dislay = ('first_name', 'last_name', 'email', 'username')
    list_filter = ('email', 'username')

admin.site.register(CustomUser, CustomUserAdmin)
