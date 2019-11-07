from django.shortcuts import render, redirect
from .models import Reservation
from main.models import ClassRoom
from main.models import Building
from .reserve_valid_chk import is_reservation_valid

def reservation(request, building_no, classroom_no):
	classroom = ClassRoom.objects.get(building_no=building_no, room_no=classroom_no)
	if request.method == "POST":
		reservation = Reservation()
		if is_reservation_valid(classroom.id, request.POST['date'], request.POST['start-time'], request.POST['end-time']):
			reservation.room_no = classroom
			reservation.start_time = request.POST['start-time']
			reservation.end_time = request.POST['end-time']
			reservation.user = request.user
			reservation.date = request.POST['date']
			reservation.save()
		return redirect('/')
	else:
		reservations = Reservation.objects.filter(room_no = classroom.id, date="2019-11-01").order_by('end_time')
		print(reservations)
		return render(request, 'reservation.html', {'classroom' : classroom, 'reservations' : reservations})

def book_manage(request):
    reservations = Reservation.objects.filter(user = request.user).order_by('-pk')
    print(reservations)
    return render(request, 'book_manage.html', {'reservations' : reservations})