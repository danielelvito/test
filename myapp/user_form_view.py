
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
        return redirect('login')  # یا هر صفحهای که میخواهید بعد از ثبت نام به آن هدایت شوید
    else:
       form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})