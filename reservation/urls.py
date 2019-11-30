from django.urls import path
from reservation import views

urlpatterns = [
    path('building/<int:building_no>/<classroom_no>/reservation/', views.reservation, name='reservation'),
    path('book-manage/', views.book_manage, name='book_manage'),
    path('manager-select-building/', views.manager_select_building, name='manager_select_building'),
    path('manager-page/<building_no>', views.manager, name='manager_page'),
    path('reservation-confirm/<int:reservation_id>', views.reservation_confirm, name='reservation_confirm'),
    path('reservation-deny/<int:reservation_id>', views.reservation_deny, name='reservation_deny'),
    path('reservation-cancel' , views.reservation_cancel, name='reservation_cancel'),
    
    path('reservation-detail/<int:pk>', views.reservationDetail.as_view(), name='detail'),
]
