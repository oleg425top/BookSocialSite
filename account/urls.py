from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import user_login, dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logout.html'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'), name='password_change_done'),
    path('', dashboard, name='dashboard'),
]