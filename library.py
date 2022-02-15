""" Word library of the app. """
#TODO:初始化字词库
WORDS = []
with open("words.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        WORDS.append(line.replace("\n", ""))

def get_library_letter_num(letter_num:int):
    result = []
    for word in WORDS:
        if len(word) == letter_num:
            result.append(word)
    return result
