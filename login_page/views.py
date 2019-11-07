from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from login_page.forms import UserForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse("Logged in Buddy!")
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login_page/login.html', {})


def register(request):
    if request.method == 'POST':
        user_form = UserForm()
        user_form.username = request.POST.get('username')
        user_form.email = request.POST.get('email')
        user_form.password = request.POST.get('password')
        user = user_form.save(commit=False)
        user.set_password(user_form.password)
        user.save()
        return HttpResponse("Registered")
    return render(request, 'login_page/register.html', {})
