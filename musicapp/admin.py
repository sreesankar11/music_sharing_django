from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import MusicFile

User = get_user_model()

# Unregister User from the default admin site
admin.site.unregister(User)

# Register your custom UserAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Customize the UserAdmin as per your requirements
    pass

# Register the MusicFile model
admin.site.register(MusicFile)

