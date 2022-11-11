from django.contrib import admin
from .models import *
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Address)
admin.site.register(Teacher, TeacherAdmin)


