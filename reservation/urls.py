from django.urls import path
from reservation import views

urlpatterns = [
    path('building/<int:building_no>/<int:classroom_no>/reservation', views.reservation, name='reservation'),
]
