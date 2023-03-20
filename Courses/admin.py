from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Teacher, Course, Bill

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ['name']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "description"]
    search_fields = ['name', 'description']


class BillAdmin(admin.ModelAdmin):

    list_display = ["id", "first_name", "last_name", "phone", "email", "curses"]
    search_fields = ['first_name']


class CourseAdmin(admin.ModelAdmin):

    list_display = ["id", "name", "price", "description", "category", "teacher", "active"]
    search_fields = ['name', 'description', 'price']






# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Bill, BillAdmin)
