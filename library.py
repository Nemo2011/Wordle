""" Word library of the app. """
import lists

# TODO:初始化字词库
WORDS = lists.WORDS
# TODO:字词库方法
def get_library_letter_num(letter_num):
    result = []
    for word in WORDS:
        if len(word) == letter_num:
            result.append(word)
    return result
