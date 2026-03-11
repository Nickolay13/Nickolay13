#Квадрат числа
number=float(input("Введите число:"))
result=number ** 2
print(f"Число {number} В КВАДРАТЕ равно {result}")

#Находим среднее трьох чисел
number1=float(input("Введите первое число:"))
number2=float(input("Введите второе число:"))
number3=float(input("Введите третье число:"))
average = (number1 + number2 + number3) / 3
print(f"Середнє арифметичне: {average}")

#перевод минут в часы
total_minutes=float(input("Введите количество минут:"))
hours=total_minutes//60
minutes=total_minutes % 60
print(f"Это составляет:,{hours},часов,{minutes},минут")

#расчет скидки
price=float(input("Введите число:"))
discount=float(input("Введите суму скидки у %:"))
result=price * (1-discount/100)
print(f"цена со скидкой: {result}")

#вывод последнего числа
number=int(input("Введите целое число:"))
result=number%10
print(f"последнее число: {result}")

#Периметр прямоугольника
number1=float(input("Введите ширину:"))
number2=float(input("Введите длину:"))
result=2*(number1+number2)
print(f"Периметр равен: {result}")

#выводим каждое число
number=int(input("Введите 4х значное число:"))
number1=number//1000
number2=(number//100)%10
number3=(number//10)%10
number4=number%10
print(f"первое число{number1}")
print(f"второе число{number2}")
print(f"третье число{number3}")
print(f"четвертое число{number4}")