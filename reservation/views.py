from django.shortcuts import render

def reservation(request, building_no, classroom_no):
    return render(request, 'reservation.html')