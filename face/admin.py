from django.contrib import admin
from django.utils.html import format_html

from face.models import UserFace, Employee, Service, Attendance


@admin.register(UserFace)
class UserfaceAdmin(admin.ModelAdmin):
    list_display = ['image_tag', "name"]
    search_fields = ['name']
    list_filter = ["created_at", "updated_at"]

    def image_tag(self, obj):
        return format_html('<img src="{}"  width="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', "name"]
    search_fields = ['name']
    list_filter = ["created_at", "updated_at"]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date', ]
    search_fields = ['date']
    list_filter = ["created_at", "updated_at"]
