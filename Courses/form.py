from django import forms
import hashlib
from django.contrib.auth.models import User
from .models import Bill
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.exceptions import ObjectDoesNotExist
import re








class RegistraionForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    captcha = ReCaptchaField()




    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản không hợp lệ")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")




    def save(self):
        name = str(hashlib.md5(self.cleaned_data['first_name'].encode('utf-8')).hexdigest())


        User.objects.create_user(username=self.cleaned_data['username'],
                                 email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password1'],
                                 first_name=name,
                                 last_name=self.cleaned_data['last_name'])



class Login_Form(forms.Form):
    def get_login(self):
        username = self.cleaned_data['password1']
        password = self.cleaned_data['password2']








