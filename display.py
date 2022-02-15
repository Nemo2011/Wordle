""" Displayer of the game. """
import sys
import pygame
#TODO:编写显示类
class Button:
    def __init__(self, wordle, x, y, color, msg, scale, width, height):
        self.scr = wordle.scr
        self.scr_rect = self.scr.get_rect()
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = [0, 0, 0]
        self.font = pygame.font.SysFont("Arial", scale)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.msg = msg
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Display texts. """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw the button. """
        self.scr.fill(self.button_color, self.rect)
        self.scr.blit(self.msg_image, self.msg_image_rect)

class Display:
    def __init__(self, wordle):
        """ Display class. """
        self.scr:pygame.Surface = wordle.scr
        self.wordle = wordle
        self.buttons = []
        self.letters = []

    def display(self):
        """ Display screen. """
        self.buttons = []
        mode = self.wordle.stats.mode
        if mode == "ask":
            for letter in range(4, 12, 1):
                y = ((letter - 3) // 4) * 100 + ((letter - 3) // 4 + 1) * 50
                x = ((letter - 3) % 4 - 1) * 100 + ((letter - 3) % 4) * 50 + 175
                if (letter - 3) % 4 == 0:
                    x = 675
                    y -= 150
                btn = Button(self.wordle, x, y, (0, 255, 0), str(letter), 35, 100, 100)
                btn.draw_button()
                self.buttons.append(btn)
            btn = Button(self.wordle, 400, 700, (255, 0, 0), "QUIT", 35, 200, 100)
            btn.draw_button()
            self.buttons.append(btn)
        else:
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(250, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(300, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(350, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(400, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(450, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(500, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(550, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(600, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(650, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(700, 650, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(275, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(325, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(375, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(425, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(475, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(525, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(575, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(625, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(675, 700, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(300, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(350, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(400, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(450, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(500, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(550, 750, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(600, 750, 50, 50))
            self.q = Button(self.wordle, 255, 655, self.wordle.stats.state['q'], "Q", 35, 40, 40)
            self.w = Button(self.wordle, 305, 655, self.wordle.stats.state['w'], "W", 35, 40, 40)
            self.e = Button(self.wordle, 355, 655, self.wordle.stats.state['e'], "E", 35, 40, 40)
            self.r = Button(self.wordle, 405, 655, self.wordle.stats.state['r'], "R", 35, 40, 40)
            self.t = Button(self.wordle, 455, 655, self.wordle.stats.state['t'], "T", 35, 40, 40)
            self.y = Button(self.wordle, 505, 655, self.wordle.stats.state['y'], "Y", 35, 40, 40)
            self.u = Button(self.wordle, 555, 655, self.wordle.stats.state['u'], "U", 35, 40, 40)
            self.i = Button(self.wordle, 605, 655, self.wordle.stats.state['i'], "I", 35, 40, 40)
            self.o = Button(self.wordle, 655, 655, self.wordle.stats.state['o'], "O", 35, 40, 40)
            self.p = Button(self.wordle, 705, 655, self.wordle.stats.state['p'], "P", 35, 40, 40)
            self.a = Button(self.wordle, 280, 705, self.wordle.stats.state['a'], "A", 35, 40, 40)
            self.s = Button(self.wordle, 330, 705, self.wordle.stats.state['s'], "S", 35, 40, 40)
            self.d = Button(self.wordle, 380, 705, self.wordle.stats.state['d'], "D", 35, 40, 40)
            self.f = Button(self.wordle, 430, 705, self.wordle.stats.state['f'], "F", 35, 40, 40)
            self.g = Button(self.wordle, 480, 705, self.wordle.stats.state['g'], "G", 35, 40, 40)
            self.h = Button(self.wordle, 530, 705, self.wordle.stats.state['h'], "H", 35, 40, 40)
            self.j = Button(self.wordle, 580, 705, self.wordle.stats.state['j'], "J", 35, 40, 40)
            self.k = Button(self.wordle, 630, 705, self.wordle.stats.state['k'], "K", 35, 40, 40)
            self.l = Button(self.wordle, 680, 705, self.wordle.stats.state['l'], "L", 35, 40, 40)
            self.z = Button(self.wordle, 305, 755, self.wordle.stats.state['z'], "Z", 35, 40, 40)
            self.x = Button(self.wordle, 355, 755, self.wordle.stats.state['x'], "X", 35, 40, 40)
            self.c = Button(self.wordle, 405, 755, self.wordle.stats.state['c'], "C", 35, 40, 40)
            self.v = Button(self.wordle, 455, 755, self.wordle.stats.state['v'], "V", 35, 40, 40)
            self.b = Button(self.wordle, 505, 755, self.wordle.stats.state['b'], "B", 35, 40, 40)
            self.n = Button(self.wordle, 555, 755, self.wordle.stats.state['n'], "M", 35, 40, 40)
            self.m = Button(self.wordle, 605, 755, self.wordle.stats.state['m'], "N", 35, 40, 40)
            self.back = Button(self.wordle, 655, 755, (255, 255, 0), "<-", 35, 40, 40)
            self.submit = Button(self.wordle, 705, 755, (255, 255, 0), "ok", 35, 40, 40)
            self.a.draw_button()
            self.b.draw_button()
            self.c.draw_button()
            self.d.draw_button()
            self.e.draw_button()
            self.f.draw_button()
            self.g.draw_button()
            self.h.draw_button()
            self.i.draw_button()
            self.j.draw_button()
            self.k.draw_button()
            self.l.draw_button()
            self.m.draw_button()
            self.n.draw_button()
            self.o.draw_button()
            self.p.draw_button()
            self.q.draw_button()
            self.r.draw_button()
            self.s.draw_button()
            self.t.draw_button()
            self.u.draw_button()
            self.v.draw_button()
            self.w.draw_button()
            self.x.draw_button()
            self.y.draw_button()
            self.z.draw_button()
            self.back.draw_button()
            self.submit.draw_button()
            for round in range(6):
                for letter in range(self.wordle.stats.letters):
                    if round + 1 >= self.wordle.stats.round:
                        num = self.wordle.stats.letters
                        x = letter * 75 + (letter + 1) * 17 + (1000 - num * 75 - (num + 1) * 17) / 2
                        y = round * 75 + (round + 1) * 8
                        if self.wordle.stats.win and round + 1 == self.wordle.stats.round:
                            pass
                        else:
                            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(x, y, 75, 75))
                        if round + 1 == self.wordle.stats.round and len(self.wordle.stats.type_word) > letter:
                            btn = Button(self.wordle, x + 5, y + 5, (255, 255, 255), self.wordle.stats.type_word[letter], 35, 65, 65)
                        else:
                            btn = Button(self.wordle, x + 5, y + 5, (255, 255, 255), "", 35, 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
                    else:
                        num = self.wordle.stats.letters
                        log_str = self.wordle.stats.log[round]
                        x = letter * 75 + (letter + 1) * 17 + (1000 - num * 75 - (num + 1) * 17) / 2
                        y = round * 75 + (round + 1) * 8
                        color = self.wordle.stats.colors[round][letter]
                        if color == "g":
                            c = (0, 255, 0)
                        elif color == "y":
                            c = (255, 255, 0)
                        else:
                            c = (125, 125, 125)
                        btn = Button(self.wordle, x + 5, y + 5, c, log_str[letter], 35, 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
                    if self.wordle.stats.win and round + 1 == self.wordle.stats.round:
                        num = self.wordle.stats.letters
                        log_str = self.wordle.stats.log[round]
                        x = letter * 75 + (letter + 1) * 17 + (1000 - num * 75 - (num + 1) * 17) / 2
                        y = round * 75 + (round + 1) * 8
                        color = self.wordle.stats.colors[round][letter]
                        if color == "g":
                            c = (0, 255, 0)
                        elif color == "y":
                            c = (255, 255, 0)
                        else:
                            c = (125, 125, 125)
                        btn = Button(self.wordle, x + 5, y + 5, c, log_str[letter], 35, 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
