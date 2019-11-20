from .models import Reservation

def is_reservation_valid(clasroom_no, date, start_time, end_time):
    reservations = Reservation.objects.filter(room_no = clasroom_no, date=date).order_by('end_time')
    print(reservations)
    for reservation in reservations:
        print(str(reservation.start_time) + "~" + str(reservation.end_time))
        #TODO 빈 시간 배정 가능 여부 판단...
    return True