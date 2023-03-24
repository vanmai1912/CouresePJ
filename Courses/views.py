import pdb

import paypalrestsdk
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from paypal.pro.forms import PaymentForm
from paypalrestsdk import Payment
from requests import session

# from paypal.pro.forms import PaymentForm
# from paypalrestsdk import Payment
from  Courses.encoding import *
from  Courses.decoding import *
from .static import *
from  captcha import *
from .form import RegistraionForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, generics, permissions
from .models import Course, Bill, Teacher, Category, Payment as PaymentModel
from .serializers import CourseSerializer,  TeacherSerializer, CategorySerializer




def login(request):
    return render(request, '.polls/layout/login.html')

# def logout(request):
#     logout(request)
#     return redirect('login')
def classes(request):
    queryset = Course.objects.all()
    return render(request, 'polls/classes.html', {'queryset': queryset})


def register(request):
    form = RegistraionForm()
    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'polls/register.html', {'form': form})





def index(request):

    return render(request, 'polls/index.html')





def paypal(request, id):
    c = Course.objects.get(id=id)
    if request.method == 'POST':
        firstname = encoding_no2(request.POST['name'])
        lastname = encoding_no2(request.POST['lastname'])
        phone = encoding_no2(request.POST['phone'])
        mail = encoding_no2(request.POST['email'])
        price = request.POST['price']
        course = request.POST['course']
        bill = Bill(first_name=firstname, last_name=lastname, phone=phone, course=course,email=mail, price=price)
        bill.save()
        return redirect('/')
    return render(request, 'polls/paypal.html', {'c': c})

# def payment(request):
#     if request.method == 'POST':
#         firstname = encoding_no2(request.POST['name'])
#         lastname = encoding_no2(request.POST['lastname'])
#         phone = encoding_no2(request.POST['phone'])
#         mail = encoding_no2(request.POST['email'])
#         price = request.POST['price']
#         course = request.POST['course']
#         bill = Bill(first_name=firstname, last_name=lastname, phone=phone, course=course,email=mail, price=price)
#         payment = paypalrestsdk.Payment({
#             "intent": "sale",
#             "payer": {
#                 "payment_method": "paypal"
#             },
#             "transactions": [{
#                 "amount": {
#                     "total": price,
#                     "currency": "USD"
#                 },
#                 "description": "Mua hàng trên Flask Shop"
#             }],
#             "redirect_urls": {
#                 "return_url": url_for('success(bill)', _external=True),
#                 "cancel_url": url_for('cart', _external=True)
#             }
#         })
#         if payment.create():
#             return payment
#         else:
#             raise ValueError(payment.error)
#         # # if payment.create():
#         #     # Lưu Payment ID vào session
#         #     session['payment_id'] = payment.id
#         #     # Redirect user đến trang thanh toán của PayPal
#         #     for link in payment.links:
#         #         if link.method == 'REDIRECT':
#         #             redirect_url = str(link.href)
#         #             return redirect(redirect_url)
#         # else:
#         #     return "Lỗi trong quá trình tạo Payment"





# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     #permission_classes = [permissions.IsAuthenticated]
#
#
# class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView,
#                   generics.RetrieveAPIView
#                   ):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
#
# class TeacherViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
#
# class registerViewSet(viewsets.ModelViewSet):
#     queryset = register.objects.all()
#     serializer_class = registerSerializer





# Create your views here.

# Create your views here.
