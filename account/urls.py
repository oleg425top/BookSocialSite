from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import user_login, dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logout.html'), name='logout'),
    path('', dashboard, name='dashboard'),
]