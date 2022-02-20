""" Button class. """
import pygame
#TODO:字体编写
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 35)
#TODO:定义类
class Button:
    def __init__(self, wordle, x, y, color, msg, width, height, txt_color=(0, 0, 0)):
        """ Button class. """
        self.scr = wordle.scr
        self.scr_rect = self.scr.get_rect()
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = txt_color
        self.font = FONT
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.msg = msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Display texts. """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw the button. """
        self.scr.fill(self.button_color, self.rect)
        self.scr.blit(self.msg_image, self.msg_image_rect)