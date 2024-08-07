from django.contrib import admin
from .models import UserAccount, Profiles


# ===============================
# Users Admin Table Display
# ===============================
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'type', 'is_active')
    list_display_links = ('id', 'first_name')
    list_editable = ('is_active',)
    list_per_page = 25
    

# ===============================
# Users Profiles Table Display
# ===============================
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name')
    list_display_links = ('id', 'user', )
    list_per_page = 25

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Profiles, ProfilesAdmin)