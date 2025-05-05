from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task
from django.contrib.auth import authenticate
CustomUser = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, "authontication/register.html")


# **User Login (Username or Email)**


def user_login(request):
    if request.method == "POST":
        login_input = request.POST.get('login_input')
        password = request.POST.get('password')

        # Try to get user by username or email
        user = CustomUser.objects.filter(username=login_input).first()
        if not user:
            user = CustomUser.objects.filter(email=login_input).first()

        # Authenticate with username and password
        if user:
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, "Login successful!")
                return redirect('home')

        messages.error(request, "Invalid username/email or password!")

    return render(request, "authontication/login.html")



# **User Logout**
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
