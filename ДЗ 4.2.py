#сумма елементов с парными индексами
def calculate (numbers):
    if not numbers:
        return 0
    elements = numbers[::2]
    sum_1 = sum(elements)
    result =  sum_1 * numbers[-1]
    return result
print(calculate([0, 1, 7, 2, 4, 8]))
print(calculate([1, 3, 5]))
print(calculate([6]))
print(calculate([]))