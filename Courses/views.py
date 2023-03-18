from django.contrib.auth import authenticate
from django.shortcuts import render
from .static import *
from .form import RegistraionForm

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets, generics, permissions
from .models import Course, Teacher,  Category
from .serializers import CourseSerializer,  TeacherSerializer, CategorySerializer


def login(request):
    return render(request, 'registration/login.html')


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
