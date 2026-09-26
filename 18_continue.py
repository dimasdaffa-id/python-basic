number = 1

while number <= 10:
    if number % 2 == 0:
        number += 1
        continue
    else:
        print(number)
        number += 1