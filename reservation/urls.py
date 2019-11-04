from django.urls import path
from reservation import views

urlpatterns = [
    path('building/<int:building_no>/<int:classroom_no>/reservation', views.reservation, name='reservation'),
    path('book-manage/', views.book_manage, name='book_manage'),
]
