from rest_framework.serializers import ModelSerializer
# <<<<<<< HEAD
from .models import Course,  Teacher, Category, Bill
# =======
from .models import Course, Teacher, Category, Payment



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

class PaymentSerializer(ModelSerializer):
        class Meta:
            model = Payment
            fields = ['payment_id', 'payer_id', 'payment_amount']



class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = ["id", "first_name", "last_name", "phone", "email", "course"]











