from django.contrib import admin
from .models import Todo,Student,Teacher


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'passed')


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'married')


admin.site.register(Teacher, TeacherAdmin)