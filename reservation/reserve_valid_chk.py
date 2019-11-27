from .models import Reservation

def is_reservation_valid(clasroom_no, date, start_time, end_time):
    reservations = Reservation.objects.filter(room_no = clasroom_no, date=date).order_by('end_time')
    timeslot = ['18', '19', '20', '21']
    available_slot = []    
    sorted(reservations, key=lambda reservation: reservation.start_time)

    if len(reservations) == 0:
        return True

    reservationIdx = 0
    start_hour = str(reservations[reservationIdx].start_time)[:2]
    end_hour = str(reservations[reservationIdx].end_time)[:2]
    is_available = True
    
    for time in timeslot:
        if reservationIdx < len(reservations): # 더이상 남은 예약이 없을 때
            reservation = reservations[reservationIdx]
            start_hour = str(reservation.start_time)[:2]

        if start_hour == time: # 예약이 잡혀있는 시간, 예약 불가능
            is_available = False
            end_hour = str(reservation.end_time)[:2]
            reservationIdx += 1

        elif end_hour == time: # 예약이 끝나는 시간, 예약 가능
            is_available = True
            end_hour = str(reservation.end_time)[:2]

        if is_available == True: # 예약 가능할 때
            available_slot.append(time)

    if len(available_slot) == 0:
        return False

    for time in range(int(str(start_time)[:2]), int(str(end_time)[:2])):
        print(time)
        if str(time) not in available_slot:
            return False
    
    return True