""" Displayer of the game. """
import sys
import pygame
import buttons
#TODO:编写显示类
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
            btn = buttons.Button(self.wordle, 0, 0, (255, 255, 255), "WORDLE GAME", 1000, 100)
            btn.draw_button()
            btn100 = buttons.Button(self.wordle, 150, 275, (0, 0, 255), "4", 100, 75, (255, 255, 255))
            btn100.draw_button()
            btn5 = buttons.Button(self.wordle, 150, 150, (0, 0, 255), "5", 700, 75, (255, 255, 255))
            btn5.draw_button()
            self.buttons.append(btn100)
            self.buttons.append(btn5)
            btn6 = buttons.Button(self.wordle, 350, 275, (0, 0, 255), "6", 100, 75, (255, 255, 255))
            btn6.draw_button()
            self.buttons.append(btn6)
            if self.wordle.stats.easy:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(545, 330, 110, 60))
                easy = buttons.Button(self.wordle, 550, 335, (0, 255, 0), "EASY", 100, 50, (255, 255, 255))
                hard = buttons.Button(self.wordle, 750, 335, (125, 125, 125), "HARD", 100, 50, (255, 255, 255))
            else:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(745, 330, 110, 60))
                easy = buttons.Button(self.wordle, 550, 335, (125, 125, 125), "EASY", 100, 50, (255, 255, 255))
                hard = buttons.Button(self.wordle, 750, 335, (0, 255, 0), "HARD", 100, 50, (255, 255, 255))
            tip = buttons.Button(self.wordle, 550, 250, (0, 0, 255), "MODE", 300, 50, (255, 255, 255))
            easy.draw_button()
            hard.draw_button()
            self.buttons.append(easy)
            self.buttons.append(hard)
            tip.draw_button()
            hlp = buttons.Button(self.wordle, 400, 400, (0, 0, 255), "HELP", 200, 100, (255, 255, 255))
            hlp.draw_button()
            btn = buttons.Button(self.wordle, 650, 400, (125, 125, 125), "QUIT", 200, 100, (255, 255, 255))
            btn.draw_button()
            btn2 = buttons.Button(self.wordle, 150, 400, (0, 0, 255), "INFO", 200, 100, (255, 255, 255))
            btn2.draw_button()
            self.buttons.append(btn)
            self.buttons.append(hlp)
            self.buttons.append(btn2)
        else:
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(250, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(300, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(350, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(400, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(450, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(500, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(550, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(600, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(650, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(700, 500, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(250, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(300, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(350, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(400, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(450, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(500, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(550, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(600, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(650, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(700, 550, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(275, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(325, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(375, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(425, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(475, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(525, 600, 50, 50))
            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(575, 600, 50, 50))
            self.q = buttons.Button(self.wordle, 255, 505, self.wordle.stats.state['q'], "Q", 40, 40)
            self.w = buttons.Button(self.wordle, 305, 505, self.wordle.stats.state['w'], "W", 40, 40)
            self.e = buttons.Button(self.wordle, 355, 505, self.wordle.stats.state['e'], "E", 40, 40)
            self.r = buttons.Button(self.wordle, 405, 505, self.wordle.stats.state['r'], "R", 40, 40)
            self.t = buttons.Button(self.wordle, 455, 505, self.wordle.stats.state['t'], "T", 40, 40)
            self.y = buttons.Button(self.wordle, 505, 505, self.wordle.stats.state['y'], "Y", 40, 40)
            self.u = buttons.Button(self.wordle, 555, 505, self.wordle.stats.state['u'], "U", 40, 40)
            self.i = buttons.Button(self.wordle, 605, 505, self.wordle.stats.state['i'], "I", 40, 40)
            self.o = buttons.Button(self.wordle, 655, 505, self.wordle.stats.state['o'], "O", 40, 40)
            self.p = buttons.Button(self.wordle, 705, 505, self.wordle.stats.state['p'], "P", 40, 40)
            self.a = buttons.Button(self.wordle, 255, 555, self.wordle.stats.state['a'], "A", 40, 40)
            self.s = buttons.Button(self.wordle, 305, 555, self.wordle.stats.state['s'], "S", 40, 40)
            self.d = buttons.Button(self.wordle, 355, 555, self.wordle.stats.state['d'], "D", 40, 40)
            self.f = buttons.Button(self.wordle, 405, 555, self.wordle.stats.state['f'], "F", 40, 40)
            self.g = buttons.Button(self.wordle, 455, 555, self.wordle.stats.state['g'], "G", 40, 40)
            self.h = buttons.Button(self.wordle, 505, 555, self.wordle.stats.state['h'], "H", 40, 40)
            self.j = buttons.Button(self.wordle, 555, 555, self.wordle.stats.state['j'], "J", 40, 40)
            self.k = buttons.Button(self.wordle, 605, 555, self.wordle.stats.state['k'], "K", 40, 40)
            self.l = buttons.Button(self.wordle, 655, 555, self.wordle.stats.state['l'], "L", 40, 40)
            self.z = buttons.Button(self.wordle, 280, 605, self.wordle.stats.state['z'], "Z", 40, 40)
            self.x = buttons.Button(self.wordle, 330, 605, self.wordle.stats.state['x'], "X", 40, 40)
            self.c = buttons.Button(self.wordle, 380, 605, self.wordle.stats.state['c'], "C", 40, 40)
            self.v = buttons.Button(self.wordle, 430, 605, self.wordle.stats.state['v'], "V", 40, 40)
            self.b = buttons.Button(self.wordle, 480, 605, self.wordle.stats.state['b'], "B", 40, 40)
            self.n = buttons.Button(self.wordle, 530, 605, self.wordle.stats.state['n'], "N", 40, 40)
            self.m = buttons.Button(self.wordle, 580, 605, self.wordle.stats.state['m'], "M", 40, 40)
            self.back = buttons.Button(self.wordle, 655, 555, (255, 255, 0), "<-", 40, 40)
            self.submit = buttons.Button(self.wordle, 705, 555, (255, 255, 0), "ok", 40, 40)
            if self.wordle.stats.cc:
                self.cc = buttons.Button(self.wordle, 800, 550, (255, 255, 0), "COPY EMOJI", 200, 100)
                self.cc.draw_button()
                self.si = buttons.Button(self.wordle, 0, 550, (255, 255, 0), "SAVE IMAGE", 200, 100)
                self.si.draw_button()
            elif (not self.wordle.stats.win) and (self.wordle.stats.round != 1) and (self.wordle.stats.round != 6 or not self.wordle.stats.win):
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(625, 600, 50, 50))
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(675, 600, 50, 50))
                self.give = buttons.Button(self.wordle, 630, 605, (0, 139, 0), "ANS", 80, 40)
                self.give.draw_button()
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
                        x = letter * 75 + (letter + 1) * 8 + (1000 - num * 75 - (num + 1) * 8) / 2
                        y = round * 75 + (round + 1) *  8
                        if self.wordle.stats.win and round + 1 == self.wordle.stats.round:
                            pass
                        else:
                            pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(x, y, 75, 75))
                        if round + 1 == self.wordle.stats.round and len(self.wordle.stats.type_word.upper()) > letter:
                            btn = buttons.Button(self.wordle, x + 5, y + 5, (255, 255, 255), self.wordle.stats.type_word.upper()[letter], 65, 65)
                        else:
                            btn = buttons.Button(self.wordle, x + 5, y + 5, (255, 255, 255), "", 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
                    else:
                        num = self.wordle.stats.letters
                        log_str = self.wordle.stats.log[round]
                        x = letter * 75 + (letter + 1) * 8 + (1000 - num * 75 - (num + 1) * 8) / 2
                        y = round * 75 + (round + 1) * 8
                        color = self.wordle.stats.colors[round][letter]
                        if color == "g":
                            c = (0, 139, 0)
                        elif color == "y":
                            c = (255, 255, 0)
                        else:
                            c = (125, 125, 125)
                        btn = buttons.Button(self.wordle, x + 5, y + 5, c, log_str[letter], 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
                    if self.wordle.stats.win and round + 1 == self.wordle.stats.round:
                        num = self.wordle.stats.letters
                        log_str = self.wordle.stats.log[round]
                        x = letter * 75 + (letter + 1) * 8 + (1000 - num * 75 - (num + 1) * 8) / 2
                        y = round * 75 + (round + 1) * 8
                        color = self.wordle.stats.colors[round][letter]
                        if color == "g":
                            c = (0, 139, 0)
                        elif color == "y":
                            c = (255, 255, 0)
                        else:
                            c = (125, 125, 125)
                        btn = buttons.Button(self.wordle, x + 5, y + 5, c, log_str[letter], 65, 65)
                        btn.draw_button()
                        self.letters.append(btn)
                self.prnsc = buttons.Button(self.wordle, 800, 700, (255, 255, 0), "SAVE", 200, 100)
