from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views.generic import DetailView
import datetime
from .models import Reservation
from main.models import ClassRoom
from main.models import Building
from .reserve_valid_chk import is_reservation_valid
from django.http import HttpResponse
from django.contrib import messages

def reservation(request, building_no, classroom_no):
	classroom = ClassRoom.objects.get(building_no=building_no, room_no=classroom_no)
	if request.method == "POST":
		#TODO 시간 formatting 함수화 시킬것, reservation form 으로 받을 것
		s_hour = request.POST['start-hour']
		e_hour = request.POST['end-hour']
		start_time = s_hour + ":00"
		end_time = e_hour + ":00"
		date = request.POST.get('date')
		reservation = Reservation()
		if is_reservation_valid(classroom.id, date, start_time, end_time):
			reservation.room_no = classroom
			reservation.start_time = start_time
			reservation.end_time = end_time
			reservation.user = request.user
			reservation.date = date
			reservation.personnel = request.POST.get('personnel')
			reservation.purpose = request.POST.get('purpose')
			reservation.room_no.building_no.add_new_request()
			reservation.save()
			return redirect('book_manage')
		else:
			messages.info(request, '예약이 불가능합니다.')
			now = datetime.datetime.now()
			reservations = Reservation.objects.filter(room_no = classroom.id, date=now.strftime('%Y-%m-%d')).order_by('end_time')
			return render(request, 'reservation.html', {'classroom' : classroom, 'reservations' : reservations, 'date' : date})
	else:
		date = request.GET['date']
		print(date)
		now = datetime.datetime.now()
		reservations = Reservation.objects.filter(room_no = classroom.id, date=now.strftime('%Y-%m-%d')).order_by('end_time')
		return render(request, 'reservation.html', {'classroom' : classroom, 'reservations' : reservations, 'date' : date})

def book_manage(request):
    reservations = Reservation.objects.filter(user = request.user).order_by('-pk')
    return render(request, 'book_manage.html', {'reservations' : reservations})

def manager_select_building(request):
	buildings1 = Building.objects.all()[0:5]
	buildings2 = Building.objects.all()[5:10]
	buildings3 = Building.objects.all()[10:15]
	buildings4 = Building.objects.all()[15:20]
			
	return render(request, 'manager_select_building.html', {'buildings1' : buildings1, 'buildings2' : buildings2, 'buildings3' : buildings3, 'buildings4' : buildings4})

def manager(request, building_no):
	# building = Building.objects.get(building_no = building_no)
	# rooms = building.entry_set.all
	# print(rooms)
	applied_reservations = Reservation.objects.filter(status=0).order_by('-id')
	confirmed_reservations = Reservation.objects.filter(status=1).order_by('-id')
	return render(request, 'manager_page.html', {'applied_reservations' : applied_reservations, 'confirmed_reservations' : confirmed_reservations, 'building_no' : building_no})

def reservation_confirm(request, reservation_id):
	update_reservation = Reservation.objects.get(id=reservation_id)
	update_reservation.room_no.building_no.sub_new_request()
	update_reservation.confirm()
	return redirect('manager_page', update_reservation.room_no.building_no.pk)

def reservation_deny(request, reservation_id):
	update_reservation = Reservation.objects.get(id=reservation_id)
	update_reservation.room_no.building_no.sub_new_request()
	update_reservation.request_deny()
	return redirect('manager_page', update_reservation.room_no.building_no.pk)

def reservation_cancel(request, reservation_id):
	reservation = get_object_or_404(Reservation, id = reservation_id)
	reservation.delete()
	return redirect('book_manage')

class reservationDetail(DetailView):
	model = Reservation
	template_name='reservation_detail.html'


def reservation_modify(request, reservation_id):
	reservation = get_object_or_404(Reservation, id = reservation_id)
	classroom = ClassRoom.objects.get(building_no=reservation.room_no.building_no.building_no, room_no=reservation.room_no.room_no)
	
	if request.method == "POST":
		s_hour = request.POST['start-hour']
		e_hour = request.POST['end-hour']
		start_time = s_hour + ":00"
		end_time = e_hour + ":00"
		reservation.room_no = classroom
		reservation.start_time = start_time
		reservation.end_time = end_time
		reservation.user = request.user
		reservation.personnel = request.POST.get('personnel')
		reservation.purpose = request.POST.get('purpose')
		reservation.room_no.building_no.add_new_request()
		reservation.update()
		return redirect('book_manage')
	else:
		reservation.request_modify()
		date = reservation.date
		print(date)
		now = datetime.datetime.now()
		reservations = Reservation.objects.filter(room_no = classroom.id, date=now.strftime('%Y-%m-%d')).order_by('end_time')
		return render(request, 'reservation_modify.html', {'classroom' : classroom, 'reservations' : reservations, 'date' : date, 'reservation_id' : reservation_id})


# # 예약 불가능시 띄워줄 메시지
# def password(request):
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(request.user, request.POST)
# 		if form.is_valid():
    # 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			messages.success(request, 'Your password was updated successfully!')  # <-
# 			return redirect('settings:password')
# 		else:
# 			messages.warning(request, 'Please correct the error below.')  # <-
# 	else:
# 		form = PasswordChangeForm(request.user)
# 	return render(request, 'profiles/change_password.html', {'form': form})