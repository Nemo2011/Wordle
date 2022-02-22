""" Copying guess colors. """
import pygame
import pyperclip
import message
#TODO:定义类
class Copy:
    def __init__(self, wordle):
        """ Copying result without emoji. """
        self.wordle = wordle
        self.message = message.Message(self.wordle)

    def copy(self):
        """ Copy emoji. """
        try:
            copy_str = ""
            for log in self.wordle.stats.colors:
                log = ''.join(log)
                log = log.replace("g", "🟩")
                log = log.replace("y", "🟨")
                log = log.replace("b", "⬛")
                copy_str = copy_str + log + "\n"
            pyperclip.copy(copy_str)
            self.wordle.display.display()
            pygame.display.flip()
            self.message._info("Copyed successfully! ")
        except:
            self.message._warning("Copying failed. Please try again. ")
