"""" Make an answer. """
import random
import lists

# TODO:初始化答案库
ANSWERS = lists.ANSWERS
# TODO:答案库方法
def get_answer_letter_num(letter_num):
    results = []
    for word in ANSWERS:
        if len(word) == letter_num:
            results.append(word)
    result = random.choice(results)
    return result
