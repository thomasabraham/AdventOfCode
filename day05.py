from sys import stdin

def decode_binary_encoding(zero_char, one_letter, value):
    result = 0
    for letter in value:
        if letter == one_letter:
            result = result * 2 + 1
        elif letter == zero_char:
            result = result * 2
        else:
            return None
    return result

highest_seat_id = 0
allocated_seats = []
for line in stdin:
    if line == '':
        break
    row = decode_binary_encoding("F", "B", line[:7])
    col = decode_binary_encoding("L", "R", line[7:10])
    seat_id = row * 8 + col
    print("Seat id of row ", row, " and column ", col, " is ", seat_id)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    allocated_seats.append(seat_id)
print("Highest seat id is ", highest_seat_id)
allocated_seats.sort()
print("Allocated seats are", allocated_seats)
previous_id = allocated_seats[0]
for seat_id in allocated_seats:
    if seat_id > previous_id +1:
        print("Free seat is ", previous_id + 1)
        break
    else:
        previous_id=seat_id
