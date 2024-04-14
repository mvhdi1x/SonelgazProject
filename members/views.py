from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('login')


class UpdateProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('all_files')

    def get_object(self, queryset=None):
        return self.request.user


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('all_files')
        else:
            messages.error(request, "Username or password is wrong, Try again please!")
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('all_files')
