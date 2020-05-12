from django.contrib import admin

# Register your models here.
from apps.users.models import UserProfile
class UserProFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile,UserProFileAdmin)