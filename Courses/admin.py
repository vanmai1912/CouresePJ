from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Teacher, Course

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ['name']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "description"]
    search_fields = ['name', 'description']


class CourseAdmin(admin.ModelAdmin):

    list_display = ["id", "name", "price", "description", "category", "teacher", "active"]
    search_fields = ['name', 'description']

class PaymentAdmin(admin.ModelAdmin):

    list_display = ["payment_id","payment_amount","payment_time","payer_id"]





# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
