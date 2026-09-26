number = int(input("Enter your number: "))

even_count = 0
odd_count = 0

for number in range (1, number + 1):
    if number % 2 == 0:
        print(number, "is even.")
        even_count += 1
    if number % 2 != 0:
        print(number, "is odd.")
        odd_count += 1
        
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)