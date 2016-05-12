def large_x_one(numbers, n):
    digits = list(str(numbers))

    result = 0
    digits.reverse()
    for i, digit in enumerate(digits):
        result += n*int(digit)*10**i

    return result


def multiply_large_number(num1, num2):
    num2_digits = list(str(num2))
    result = 0
    num2_digits.reverse()
    for i, digit in enumerate(num2_digits):
        result += large_x_one(num1, int(digit))*10**i

    return result
