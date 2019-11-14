from django.shortcuts import render, redirect
import datetime
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
		now = datetime.datetime.now()
		reservations = Reservation.objects.filter(room_no = classroom.id, date=now.strftime('%Y-%m-%d')).order_by('end_time')
		print(reservations)
		return render(request, 'reservation.html', {'classroom' : classroom, 'reservations' : reservations})

def book_manage(request):
    reservations = Reservation.objects.filter(user = request.user).order_by('-pk')
    print(reservations)
    return render(request, 'book_manage.html', {'reservations' : reservations})

def manager(request):
	applied_reservations = Reservation.objects.filter(status=0).order_by('-id')
	confirmed_reservations = Reservation.objects.filter(status=1).order_by('-id')
	return render(request, 'manager_page.html', {'applied_reservations' : applied_reservations, 'confirmed_reservations' : confirmed_reservations})

def reservation_confirm(request, reservation_id):
	update_reservation = Reservation.objects.get(id=reservation_id)
	update_reservation.status = 1
	update_reservation.save()
	return redirect('manager_page')