numbers = [13,44,26,14,67,574,3457]

def get_min(numbers):
    result = numbers[0]
    for num in numbers:
            if result > num:
                result = num
            return result
min_number = get_min(numbers)
print("Min number: ", min_number)