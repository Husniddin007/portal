from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Category, Application

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = "Portal Admin"
admin.site.site_header = "Portal"
admin.site.index_title = "Portal Admin"
admin.site.site_brand = "Portal"
admin.site.copyright = "Portal"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)

#
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'series', 'jshshir', 'phone', 'category',)
    list_display_links = ('name', 'surname', 'phone', 'category',)


admin.site.register(Application, ApplicationAdmin)
