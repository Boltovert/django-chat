from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ChannelSidebar


class ChannelSidebarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(ChannelSidebar, ChannelSidebarAdmin)