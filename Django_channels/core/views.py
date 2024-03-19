from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # `form.save()` returns the user object
            login(request, user)  # Log in the user directly
            return redirect('chat:chat_index')
        else:
            # If the form is not valid, render the registration page again with the form.
            # This will display the form errors on the page.
            return render(request, 'chat/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("chat:chat_index")
    else:
        form = AuthenticationForm()
    return render(request, "chat/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def index(request):
    return render(request, "chat/index.html")
