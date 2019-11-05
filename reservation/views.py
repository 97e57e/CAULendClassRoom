from django.shortcuts import render, redirect
from .models import Reservation

def reservation(request, building_no, classroom_no):
        return render(request, 'reservation.html')

def book_manage(request):
    reservations = Reservation.objects.filter(user = request.user).order_by('-pk')
    print(reservations)
    return render(request, 'book_manage.html', {'reservations' : reservations})