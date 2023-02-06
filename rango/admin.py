from django.contrib import admin
from rango.models import Category, Page

# add more classes here like below for the admin page making sure its also imported


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
