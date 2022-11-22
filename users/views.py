from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse

from users.froms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
    return render(request, template_name='users/dashboard.html')

def register(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse('user_dashboard'))
        
    elif request.method=='GET':
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, template_name='registration/register.html', context=context)