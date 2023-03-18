from rest_framework.serializers import ModelSerializer
from .models import Course,  Teacher, Category


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name", "phone", "email", "description"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CourseSerializer(ModelSerializer):
    teacher = TeacherSerializer()
    category = CategorySerializer()
    class Meta:
        model = Course
        fields = ["id", "name", "description", "price", "teacher", "category"]











