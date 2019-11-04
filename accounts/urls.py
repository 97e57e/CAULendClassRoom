from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup-done/', views.signup_done.as_view(), name='signup_done'),
    path('signin/', views.signin, name='signin'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('my_info', views.my_info, name='my_info'),
    path('edit_info', views.edit_info, name='edit_info'),
    path('request_edit_info', views.request_edit_info, name='request_edit_info'),
    path('edit_done', views.edit_done, name='edit_done'),
]
