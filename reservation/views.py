from django.shortcuts import render, redirect
from .models import Reservation
from main.models import ClassRoom
from main.models import Building
from .reserve_valid_chk import is_reservation_valid

def reservation(request, building_no, classroom_no):
	classroom = ClassRoom.objects.get(building_no=building_no, room_no=classroom_no)
	if request.method == "POST":
		#TODO 시간 formatting 함수화 시킬것, reservation form 으로 받을 것
		s_hour = request.POST['start-hour']
		s_min = request.POST['start-min']
		e_hour = request.POST['end-hour']
		e_min = request.POST['end-min']
		start_time = s_hour + ":" + s_min
		end_time = e_hour + ":" + e_min
		reservation = Reservation()
		if is_reservation_valid(classroom.id, request.POST['date'], start_time, end_time):
			reservation.room_no = classroom
			reservation.start_time = start_time
			reservation.end_time = end_time
			reservation.user = request.user
			reservation.date = request.POST['date']
			reservation.save()
		return redirect('book_manage')
	else:
		reservations = Reservation.objects.filter(room_no = classroom.id, date="2019-11-01").order_by('end_time')
		print(reservations)
		return render(request, 'reservation.html', {'classroom' : classroom, 'reservations' : reservations})

def book_manage(request):
    reservations = Reservation.objects.filter(user = request.user).order_by('-pk')
    print(reservations)
    return render(request, 'book_manage.html', {'reservations' : reservations})