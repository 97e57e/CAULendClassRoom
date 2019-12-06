from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Building
from .models import ClassRoom
from .valid_floor_range import get_valid_floor_range, get_int_floor
from reservation.reserve_valid_chk import is_reservation_valid

def index(request):
    buildings = Building.objects.all()
    return render(request, 'index.html', {'buildings' : buildings})

def building(request, building_no, floor):
    int_floor = get_int_floor(floor)
    building = get_object_or_404(Building, pk=building_no)
    rooms = building.classroom_set.filter(floor=int_floor).order_by('room_no')
    valid_floor_range = get_valid_floor_range(building)
    return render(request, 'building.html', {'building' : building, 'rooms' : rooms, 'current_floor' : floor, 'range' : valid_floor_range})
    
def classroom(request, building_no, classroom_no):
    classroom = get_object_or_404(ClassRoom, building_no=building_no, room_no=classroom_no)
    return render(request, 'classroom.html', {'classroom' : classroom, 'room_name' : classroom.__str__})

def search(request):
    buildings = Building.objects.all()
    date = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    building = get_object_or_404(Building, building_no = request.POST.get('building'))
    rooms = building.classroom_set.all().order_by('room_no')
    searched_room = []
    for room in rooms:
        if is_reservation_valid(room, request.POST.get('date'),request.POST.get('start_time'), request.POST.get('end_time')):
            searched_room.append(room.room_no)
    room_queryset = ClassRoom.objects.filter(building_no = building.building_no, room_no__in=searched_room)
    return render(request, 'search.html', {'date' : date, 'start_time' : start_time, 'end_time' : end_time, 'buildings' : buildings, 'selected_building' : building, 'searched_room' : room_queryset})