from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def register_view(request):
    """Представление регистрации пользователя"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, auth_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))
