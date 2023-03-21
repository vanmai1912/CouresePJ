from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

# from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views


# router = DefaultRouter()
# router.register("categories", views.CategoryViewSet)
# router.register("courses", views.CourseViewSet)
# router.register("users", views.UserViewSet)
# router.register("teachers", views.TeacherViewSet)
# router.register("register", views.registerViewSet)


urlpatterns = [
    path('', views.index, name=''),
    path('login/', LoginView.as_view(), name='login'),
    path('classes/', views.classes, name="classes"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls, name='admin'),

    path('classes/<int:id>/', views.paypal, name='paypal'),


]
