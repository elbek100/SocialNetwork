import requests
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, hashers, logout
from django.contrib import messages
from django.views import View

User = get_user_model()


class LoginView(View):
    template_name = 'auth/sign_in.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username or password is not valid !!!')
            return render(request, self.template_name, self.context)


class RegisterView(View):
    template_name = 'auth/sign_up.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        first_name = request.POST.get('firstname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2 and len(password2) > 7:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!!!')
                return render(request, self.template_name, self.context)
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!!!')
                return render(request, self.template_name, self.context)
            else:
                user = User.objects.create(
                    email=email,
                    username=username,
                    password=hashers.make_password(password1)
                )
                user.first_name = first_name
                user.save()
                return redirect('sign_in')
        else:
            messages.error(request, 'Password error!!!')
            return render(request, self.template_name, self.context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('sign_in')
