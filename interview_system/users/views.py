# Create your views here.
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm()
    return render(request, 'users/create_user.html', {'form': form})