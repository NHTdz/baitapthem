def count_chars(str):
    result = 0
    for char in str:
        result += 1
    return result
input_str = input('Your string: ')
print('Length: ', count_chars(input_str))