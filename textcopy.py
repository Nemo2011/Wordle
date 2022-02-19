""" Copying guess colors. """
import pyperclip
#TODO:定义类
class Copy:
    def __init__(self, wordle):
        """ Copying result without emoji. """
        self.wordle = wordle

    def copy(self):
        """ Copy emoji. """
        copy_str = ""
        for log in self.wordle.stats.colors:
            log = ''.join(log)
            log = log.replace("g", "🟩")
            log = log.replace("y", "🟨")
            log = log.replace("b", "⬜")
            copy_str = copy_str + log + "\n"
        pyperclip.copy(copy_str)
