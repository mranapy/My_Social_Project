from django.contrib import admin
from App_Login.models import UserProfile,Follow
# Register your models here.
# @admin.register(UserProfile)
# class UserProfileModelAdmin(admin.ModelAdmin):
#     list_display = ['user','profile_pic', 'dob', 'website', 'facebook']

admin.site.register(UserProfile)
admin.site.register(Follow)

