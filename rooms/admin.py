from django.contrib import admin
from .models import Category, Room, Message


# ===============================
# Category Admin Table Display
# ===============================
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 25


# ===============================
# Room Admin Table Display
# ===============================
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'name', 'category', 'created_at')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message)