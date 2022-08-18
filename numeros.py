numbers = [55, 4 , 99, 200, 0 ,1 , 33, 66, 44, 47]

max_value = None

for num in numbers:
    if (max_value is None or num > max_value):
        max_value = num

print("Valor maxímo:", max_value)
