from django.shortcuts import render, get_object_or_404
from .models import Building
from .models import ClassRoom

def index(request):
    return render(request, 'index.html')

def building(request, building_no):
    building = get_object_or_404(Building, pk=building_no)
    return render(request, 'building.html', {'building' : building})

def classroom(request, building_no, classroom_no):
    classroom = get_object_or_404(ClassRoom, building_no=building_no, room_no=classroom_no)
    return render(request, 'classroom.html', {'classroom' : classroom, 'room_name' : classroom.__str__})