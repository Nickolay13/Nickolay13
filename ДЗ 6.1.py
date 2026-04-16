import string
def get_range(user_input):
    start, end = user_input.split('-')
    letters = string.ascii_uppercase + string.ascii_lowercase
    start_idx = letters.index(start)
    end_idx = letters.index(end)
    return letters[start_idx: end_idx + 1]
print(get_range(input()))