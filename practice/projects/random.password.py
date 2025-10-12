import random

characters= "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
char_list = []
for char in characters:
    char_list.append(char)

# print(char_list)
random.shuffle(char_list)
# print(char_list)
text = "".join(char_list)
print(text)
