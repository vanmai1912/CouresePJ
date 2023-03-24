import pdb

import paypalrestsdk
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from paypal.pro.forms import PaymentForm
from paypalrestsdk import Payment
from requests import session

# from paypal.pro.forms import PaymentForm
# from paypalrestsdk import Payment
from Courses.encoding import *
from Courses.decoding import *
from .static import *
from captcha import *

from django.core.mail import send_mail
from .form import RegistraionForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from rest_framework import viewsets, generics, permissions
from .models import Course, Bill, Teacher, Category, Payment as PaymentModel
from .serializers import CourseSerializer,  TeacherSerializer, CategorySerializer




def login(request):
    return render(request, '.polls/layout/login.html')

# def logout(request):
#     logout(request)
#     return redirect('login')
def classes(request):
    queryset = Course.objects.filter(active=True)
    if request.method == 'POST':
        search = request.POST['search']
        if search != '':
            queryset = Course.objects.filter((Q(name__icontains=search) | Q(category__name__icontains=search)
                                             | Q(teacher__name__icontains=search)) & Q(active=True))
    return render(request, 'polls/classes.html', {'queryset': queryset})


def register(request):
    form = RegistraionForm()

    if request.method == 'POST':
        form = RegistraionForm(request.POST)
         # địa chỉ email của người dùng đăng ký
        if form.is_valid():
            # subject = 'Welcome to X6EngLish'
            # message = 'Thank you for registering on our site!'
            # from_email = 'Phantan01062002@gmail.com'  # email của bạn
            # recipient_list = [mail]
            # send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'polls/register.html', {'form': form})





def index(request):

    return render(request, 'polls/index.html')





def paypal(request, id):
    c = Course.objects.get(id=id)


    # get
    #filter
    #all()

    # if request.method == 'POST':
    #     payment_id = request.POST.get('payment_id')
    #     payment = Payment.find(payment_id)
    #     if payment.state == 'approved':
    #         if payment.payer.payer_info.email.endswith('sb-ofp47n25314048@personal.example.com'):
    #             payment_info = payment.to_dict()
    #             payment_model = PaymentModel(
    #                 payment_id=payment_info['id'],
    #                 payer_id=payment_info['payer']['payer_info']['payer_id'],
    #                 payment_amount=payment_info['transactions'][0]['amount']['total']
    #             )
    #             payment_model.save()
    #             return HttpResponse('Thanh toán thành công')
    #         else:
    #             error_message = 'Thanh toán không thành công'
    #     else:
    #         error_message = 'Thanh toán không thành công'
    # else:
    #     form = PaymentForm()
    #     error_message = None


    if request.method == 'POST':
        firstname = encoding_no2(request.POST['name'])
        lastname = encoding_no2(request.POST['lastname'])
        phone = encoding_no2(request.POST['phone'])
        mail = encoding_no2(request.POST['email'])
        price = request.POST['price']
        course = request.POST['course']
        bill = Bill(first_name=firstname, last_name=lastname, phone=phone, course=course, email=mail, price=price)
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
