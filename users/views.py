from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #message.debug or messgae.info or message.success message.warning message.eroor
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
