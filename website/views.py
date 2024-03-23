from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In!")
            # Redirect to a different view after successful login
            return redirect('home')  # Update 'dashboard' with your desired URL name
        else:
            messages.error(request, "There was an Error while Logging In, please try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out..")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
