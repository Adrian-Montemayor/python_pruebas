def calculate_fibonacci(num):
    if num < 2:
        return num
    else:
        return calculate_fibonacci(num - 1) + calculate_fibonacci(num - 2)


def get_fibbonaci_sequence(num):
    for i in range(0,num + 1):
        print(calculate_fibonacci(i), end=" ")

get_fibbonaci_sequence(5)