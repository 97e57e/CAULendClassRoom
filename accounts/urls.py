from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup-done/', views.signup_done.as_view(), name='signup_done'),
    path('signin/', views.signin, name='signin'),
    path('my_info', views.my_info, name='my_info'),
    path('edit_info', views.edit_info, name='edit_info'),
]
