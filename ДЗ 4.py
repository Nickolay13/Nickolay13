#нули в конец
def zero(number):
    no_zero = [x for x in number if x !=0]
    zero_count = number.count(0)
    return no_zero + [0] * zero_count
print(zero([0, 1, 0, 12, 3]))
print(zero([0]))
print(zero([1, 0, 13, 0, 0, 0, 5]))
print(zero([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))