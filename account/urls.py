from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import user_login, dashboard, register

urlpatterns = [
    # path('login/', user_login, name='login'),
    # url-адреса входа и выхода
    path('login/',
         auth_views.LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='account/registration/logout.html'), name='logout'),
    # url-адреса смены пароля
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),
         name='password-change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),
         name='password_change_done'),

    # url-адреса сброса пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'),
         name='password_reset_complete'),



    # ...
    # path('account/password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('account/password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('account/password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('account/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('',include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),

]
