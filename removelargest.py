numbers = [0, 44,98, 20, 102, 40, 2]

def remove_largest_number(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    numbers.remove(largest)


remove_largest_number(numbers)
print(numbers)