from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . import forms
# from main.models import Log

# Create your views here.

def login_page(request):
    
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None: 
                login(request, user)
                # Log.objects.create(client = user.email , activity = request.get_full_path())
                return redirect('home')
            else:
                message = "Identifiant incorrect"
    return render(request, 'authentication/login.html', context={'form' : form, 'message' : message})

def logout_page(request):
    # Log.objects.create(client = request.user.email , activity = request.get_full_path())
    logout(request)
    return redirect('login')


