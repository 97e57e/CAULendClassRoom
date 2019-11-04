from django.shortcuts import render, get_object_or_404
from .models import Building
from .models import ClassRoom

def index(request):
    buildings = Building.objects.all()
    return render(request, 'index.html', {'buildings' : buildings})

def building(request, building_no, floor):
    building = get_object_or_404(Building, pk=building_no)
    rooms = ClassRoom.objects.filter(building_no=building_no, floor=floor)
    return render(request, 'building.html', {'building' : building, 'rooms' : rooms, 'range' : range(1, building.max_floor+1)})

def classroom(request, building_no, classroom_no):
    classroom = get_object_or_404(ClassRoom, building_no=building_no, room_no=classroom_no)
    return render(request, 'classroom.html', {'classroom' : classroom, 'room_name' : classroom.__str__})