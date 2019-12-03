def get_valid_floor_range(building):
    floor_range = range(building.min_floor, building.max_floor+1)
    valid_floor_range = []
    for floor in floor_range:
        if floor < 0:
            valid_floor_range.append('B' + str(floor)[1:])
        elif floor > 0:
            valid_floor_range.append(str(floor))
    return valid_floor_range

def get_int_floor(floor):
    int_floor = 0
    if floor[0] == 'B':
        int_floor = int('-'+floor[1])
    else:
        int_floor = floor
    return int_floor