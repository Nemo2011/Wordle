""" Save image for the game result. """
from tkinter import filedialog
import pygame
import message
#TODO:定义类
class ImageSave:
    def __init__(self, wordle):
        """ Save result with image. """
        self.wordle = wordle
        self.message = message.Message(self.wordle)

    def save(self):
        """ Save image. """
        new_rct = pygame.Rect(0, 0, 1000, 550)
        new_sur = pygame.Surface((1000, 550))
        self.wordle.display.display()
        new_sur.blit(self.wordle.scr, new_rct)
        try:
            local = filedialog.asksaveasfilename(filetypes=[("All files", ".*")])
            pygame.image.save(new_sur, local)
            self.wordle.display.display()
            pygame.display.flip()
            self.message._info("Saved successfully! ")
        except Exception as e:
            self.wordle.display.display()
            pygame.display.flip()
            self.message._info("Saving failed. Please try again. ")
