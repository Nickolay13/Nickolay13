#Список из 3 элементов
import random
length = random.randint(3,10)
original_list = [random.randint(1,100) for _ in range(length)]
new_list = [original_list [0],original_list [2], original_list [-3]]
print(f"начальный список (номер {length}): {original_list}")
print(f"новый список [номер]: {new_list}")
