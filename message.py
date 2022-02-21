""" Show message box. """
import pygame
import buttons
#TODO:定义类
class Message:
    def __init__(self, wordle):
        self.wordle = wordle
        self.scr = wordle.scr

    def _info(self, msg):
        """ Show info message. """
        pygame.display.set_caption(msg)
        going = True
        while going:
            self.msg_text = buttons.FONT.render(msg, True, (0, 0, 0), (255, 255, 255))
            self.msg_rect = self.msg_text.get_rect()
            self.msg_rect.centerx = self.scr.get_rect().centerx
            self.msg_rect.y = 200
            width = self.msg_rect.width
            pygame.draw.rect(self.scr, (125, 125, 125), pygame.Rect(500 - width / 2, 200, width, 200))
            self.scr.blit(self.msg_text, self.msg_rect)
            pygame.draw.circle(self.scr, (0, 0, 255), (425, 300), 25, 25)
            i = buttons.Button(self.wordle, 410, 285, (0, 0, 255), "i", 30, 30)
            i.draw_button()
            ok = buttons.Button(self.wordle, 505, 275, (0, 139, 0), "OK", 100, 50)
            ok.draw_button()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ok.rect.collidepoint(pos):
                        going = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        going = False
                    elif event.key == pygame.K_ESCAPE:
                        going = False
                elif event.type == pygame.QUIT:
                    going = False
        self.wordle.display.display()
        pygame.display.flip()
        pygame.display.set_caption("Wordle")

    def _warning(self, msg, important = ""):
        """ Show warning message. """
        pygame.display.set_caption(msg)
        going = True
        while going:
            self.msg_text = buttons.FONT.render(msg, True, (0, 0, 0), (255, 255, 255))
            self.msg_rect = self.msg_text.get_rect()
            self.msg_rect.centerx = self.scr.get_rect().centerx
            self.msg_rect.y = 200
            width = self.msg_rect.width
            pygame.draw.rect(self.scr, (125, 125, 125), pygame.Rect(500 - width / 2, 200, width, 200))
            self.scr.blit(self.msg_text, self.msg_rect)
            btn = buttons.Button(self.wordle, 500 - width / 2, 350, (125, 125, 125), important, width, 50, (255, 255, 255))
            btn.draw_button()
            pygame.draw.line(self.scr, (255, 0, 0), (400, 275), (450, 325), 5)
            pygame.draw.line(self.scr, (255, 0, 0), (400, 325), (450, 275), 5)
            ok = buttons.Button(self.wordle, 505, 275, (255, 0, 0), "OK", 100, 50)
            ok.draw_button()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ok.rect.collidepoint(pos):
                        going = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        going = False
                    elif event.key == pygame.K_ESCAPE:
                        going = False
                elif event.type == pygame.QUIT:
                    going = False
        self.wordle.display.display()
        pygame.display.flip()
        pygame.display.set_caption("Wordle")
