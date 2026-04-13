import string
def create_hashtag(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    words = clean_text.split()
    cap_wards = [word.capitalize() for word in words]
    hashtags = "#" + "".join(cap_wards)
    if len (hashtags) > 140:
        hashtags = hashtags[:140]
        return hashtags
user_input = input("введите слово: ")
result = create_hashtag(user_input)
print(f"Your hashtag is: {result}")