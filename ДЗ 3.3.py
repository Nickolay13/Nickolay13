# Розділити один список на два списки
def split_list(original_list):
    length = len(original_list)
    middle = (length + 1) // 2
    left_part = original_list[:middle]
    right_part = original_list[middle:]
    return [left_part, right_part]

print(f"[1, 2, 3, 4, 5, 6] => {split_list([1, 2, 3, 4, 5, 6])}")
print(f"[1, 2, 3] => {split_list([1, 2, 3])}")
print(f"[1, 2, 3, 4, 5] => {split_list([1, 2, 3, 4, 5])}")
print(f"[1] => {split_list([1])}")
print(f"[] => {split_list([])}")