from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('building/<int:building_no>/<floor>', views.building, name='building'),
    path('building/<int:building_no>/<classroom_no>/', views.classroom, name='classroom'),
    path('search/', views.search, name='search'),
]
