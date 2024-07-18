def double(listing):
    position = 0
    while position < len(listing):
        listing[position] *= 2
        position += 1


values = [6, 3, 9, 1, 0, 2]
double(values)
print(values)
