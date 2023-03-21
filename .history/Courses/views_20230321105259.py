from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from paypal.pro.forms import PaymentForm
from paypalrestsdk import Payment

from .static import *
from .form import RegistraionForm

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, generics, permissions
from .models import Course, Teacher, Category, Payment as PaymentModel
from .serializers import CourseSerializer,  TeacherSerializer, CategorySerializer


def login(request):
    return render(request, 'registration/login.html')

# def logout(request):
#     logout(request)
#     return redirect('login')
def classes(request):
    queryset = queryset = Course.objects.all()
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




def payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('payment_id')
        payment = Payment.find(payment_id)
        if payment.state == 'approved':
            if payment.payer.payer_info.email.endswith('sb-ofp47n25314048@personal.example.com'):
                payment_info = payment.to_dict()
                payment_model = PaymentModel(
                    payment_id=payment_info['id'],
                    payer_id=payment_info['payer']['payer_info']['payer_id'],
                    payment_amount=payment_info['transactions'][0]['amount']['total']
                )
                payment_model.save()
                return HttpResponse('Thanh toán thành công')
            else:
                error_message = 'Thanh toán không thành công'
        else:
            error_message = 'Thanh toán không thành công'
    else:
        form = PaymentForm()
        error_message = None
    return render(request, 'Classes.html', {'form': form, 'error_message': error_message})




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
