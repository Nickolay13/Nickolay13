#Калькулятор
print("Easy Calculator")
number1 = float(input("Введите число:"))
operation =input("Введите действие (+,-,*,/):")
number2 = float(input("Введите второе число:"))
if operation=='+':
    result=number1 + number2
elif operation=='-':
    result = number1 - number2
elif operation=='/':
    result = number1 / number2
elif operation=='*':
    result = number1 * number2
print (f"Результат {number1} {operation} {number2} = {result}")
