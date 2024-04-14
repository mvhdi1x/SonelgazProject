from django.urls import path
from members import views
from django.contrib.auth import views as auth_views

from members.views import PasswordsChangeView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UpdateProfileView.as_view(), name='edit_profile'),
    path('login_user/', views.login_user, name='login'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),
]
