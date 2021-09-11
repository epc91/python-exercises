def factorial(number):
    if type(number) != int or number < 0:
        raise ValueError('error')
    else:
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i
        return fact
