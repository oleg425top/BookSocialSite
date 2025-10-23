from django.urls import path

from account.views import user_login, dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
]