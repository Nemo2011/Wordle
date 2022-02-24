""" Displayer of the game. """
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
        self.mode = pygame.Rect(0, 0, 0, 0)

    def display(self):
        """ Display screen. """
        self.buttons = []
        mode = self.wordle.stats.mode
        if mode == "ask":
            lst = self.wordle.stats.coord
            x = lst[1]
            y = lst[0]
            btn = buttons.Button(self.wordle, 0, 0, (230, 230, 230), "WORDLE GAME", 1000, 100)
            btn.draw_button()
            if y == 2 and x == 1:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(145, 270, 185, 85))
            btn100 = buttons.Button(self.wordle, 150, 275, (0, 0, 255), "4", 175, 75, (255, 255, 255))
            btn100.draw_button()
            if y == 1:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(145, 145, 710, 85))
            btn5 = buttons.Button(self.wordle, 150, 150, (0, 0, 255), "5", 700, 75, (255, 255, 255))
            btn5.draw_button()
            self.buttons.append(btn100)
            self.buttons.append(btn5)
            if y == 2 and x == 2:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(345, 270, 185, 85))
            btn6 = buttons.Button(self.wordle, 350, 275, (0, 0, 255), "6", 175, 75, (255, 255, 255))
            btn6.draw_button()
            self.buttons.append(btn6)
            self.mode = pygame.Rect(535, 240, 330, 150)
            if y == 2 and x == 3:
                if not self.wordle.stats.select_m:
                    self.wordle.stats.easy = True
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(535, 240, 330, 150))
                pygame.draw.rect(self.scr, (230, 230, 230), pygame.Rect(540, 245, 320, 140))
            elif y == 2 and x == 4:
                if not self.wordle.stats.select_m:
                    self.wordle.stats.easy = False
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(535, 240, 330, 150))
                pygame.draw.rect(self.scr, (230, 230, 230), pygame.Rect(540, 245, 320, 140))
            if self.wordle.stats.easy:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(545, 320, 110, 60))
                easy = buttons.Button(self.wordle, 550, 325, (0, 255, 0), "OFF", 100, 50, (255, 255, 255))
                hard = buttons.Button(self.wordle, 750, 325, (125, 125, 125), "ON", 100, 50, (255, 255, 255))
            else:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(745, 320, 110, 60))
                easy = buttons.Button(self.wordle, 550, 325, (125, 125, 125), "OFF", 100, 50, (255, 255, 255))
                hard = buttons.Button(self.wordle, 750, 325, (0, 255, 0), "ON", 100, 50, (255, 255, 255))
            tip2 = buttons.Button(self.wordle, 0, 600, (255, 255, 255), "*Hard mode need: Green stay fixed, yellow be reused. ", 1000, 50)
            tip2.draw_button()
            tip = buttons.Button(self.wordle, 550, 250, (125, 125, 125), "HARD MODE", 300, 50, (255, 255, 255))
            easy.draw_button()
            hard.draw_button()
            self.buttons.append(easy)
            self.buttons.append(hard)
            tip.draw_button()
            if y == 3 and x == 2:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(275, 395, 210, 110))
            hlp = buttons.Button(self.wordle, 280, 400, (0, 0, 255), "GUIDE", 200, 100, (255, 255, 255))
            hlp.draw_button()
            if y == 3 and x == 4:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(755, 395, 210, 110))
            btn = buttons.Button(self.wordle, 760, 400, (125, 125, 125), "QUIT", 200, 100, (255, 255, 255))
            btn.draw_button()
            if y == 3 and x == 1:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(35, 395, 210, 110))
            btn2 = buttons.Button(self.wordle, 40, 400, (0, 0, 255), "INFO", 200, 100, (255, 255, 255))
            btn2.draw_button()
            if y == 3 and x == 3:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(515, 395, 210, 110))
            aut = buttons.Button(self.wordle, 520, 400, (0, 0, 255), "AUTHOR", 200, 100, (255, 255, 255))
            aut.draw_button()
            self.buttons.append(btn)
            self.buttons.append(hlp)
            self.buttons.append(aut)
            self.buttons.append(btn2)
        else:
            if self.wordle.stats.cc:
                pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0, 500, 1000, 150))
                btn = buttons.Button(self.wordle, 0, 500, (255, 255, 255), "ans", 100, 75, (125, 125, 235))
                ans = buttons.Button(self.wordle, 100, 500, (0, 0, 255), self.wordle.stats.answer.upper(), 900, 75, (255, 255, 255))
                if self.wordle.stats.col != 0:
                    pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(self.wordle.stats.col * 330 - 330, 575, 340, 75))
                self.cc = buttons.Button(self.wordle, 10, 585, (0, 139, 0), "Share result emoji", 320, 55, (0, 0, 0), True)
                self.cc.draw_button()
                self.si = buttons.Button(self.wordle, 340, 585, (197, 180, 102), "Share result image", 320, 55, (0, 0, 0), True)
                self.si.draw_button()
                self.bck = buttons.Button(self.wordle, 670, 585, (125, 125, 125), "BACK", 320, 55)
                self.bck.draw_button()
                btn.draw_button()
                ans.draw_button()
            else:
                pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(250, 500, 500, 150))
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
                self.a = buttons.Button(self.wordle, 280, 555, self.wordle.stats.state['a'], "A", 40, 40)
                self.s = buttons.Button(self.wordle, 330, 555, self.wordle.stats.state['s'], "S", 40, 40)
                self.d = buttons.Button(self.wordle, 380, 555, self.wordle.stats.state['d'], "D", 40, 40)
                self.f = buttons.Button(self.wordle, 430, 555, self.wordle.stats.state['f'], "F", 40, 40)
                self.g = buttons.Button(self.wordle, 480, 555, self.wordle.stats.state['g'], "G", 40, 40)
                self.h = buttons.Button(self.wordle, 530, 555, self.wordle.stats.state['h'], "H", 40, 40)
                self.j = buttons.Button(self.wordle, 580, 555, self.wordle.stats.state['j'], "J", 40, 40)
                self.k = buttons.Button(self.wordle, 630, 555, self.wordle.stats.state['k'], "K", 40, 40)
                self.l = buttons.Button(self.wordle, 680, 555, self.wordle.stats.state['l'], "L", 40, 40)
                self.z = buttons.Button(self.wordle, 305, 605, self.wordle.stats.state['z'], "Z", 40, 40)
                self.x = buttons.Button(self.wordle, 355, 605, self.wordle.stats.state['x'], "X", 40, 40)
                self.c = buttons.Button(self.wordle, 405, 605, self.wordle.stats.state['c'], "C", 40, 40)
                self.v = buttons.Button(self.wordle, 455, 605, self.wordle.stats.state['v'], "V", 40, 40)
                self.b = buttons.Button(self.wordle, 505, 605, self.wordle.stats.state['b'], "B", 40, 40)
                self.n = buttons.Button(self.wordle, 555, 605, self.wordle.stats.state['n'], "N", 40, 40)
                self.m = buttons.Button(self.wordle, 605, 605, self.wordle.stats.state['m'], "M", 40, 40)
                self.back = buttons.Button(self.wordle, 255, 605, (125, 125, 125), "<-", 40, 40, (255, 255, 255))
                if self.wordle.stats.state['a'] != (255, 255, 255):
                    self.a.text_color = [255, 255, 255]
                if self.wordle.stats.state['b'] != (255, 255, 255):
                    self.b.text_color = [255, 255, 255]
                if self.wordle.stats.state['c'] != (255, 255, 255):
                    self.c.text_color = [255, 255, 255]
                if self.wordle.stats.state['d'] != (255, 255, 255):
                    self.d.text_color = [255, 255, 255]
                if self.wordle.stats.state['e'] != (255, 255, 255):
                    self.e.text_color = [255, 255, 255]
                if self.wordle.stats.state['f'] != (255, 255, 255):
                    self.f.text_color = [255, 255, 255]
                if self.wordle.stats.state['g'] != (255, 255, 255):
                    self.g.text_color = [255, 255, 255]
                if self.wordle.stats.state['h'] != (255, 255, 255):
                    self.h.text_color = [255, 255, 255]
                if self.wordle.stats.state['i'] != (255, 255, 255):
                    self.i.text_color = [255, 255, 255]
                if self.wordle.stats.state['j'] != (255, 255, 255):
                    self.j.text_color = [255, 255, 255]
                if self.wordle.stats.state['k'] != (255, 255, 255):
                    self.k.text_color = [255, 255, 255]
                if self.wordle.stats.state['l'] != (255, 255, 255):
                    self.l.text_color = [255, 255, 255]
                if self.wordle.stats.state['m'] != (255, 255, 255):
                    self.m.text_color = [255, 255, 255]
                if self.wordle.stats.state['n'] != (255, 255, 255):
                    self.n.text_color = [255, 255, 255]
                if self.wordle.stats.state['o'] != (255, 255, 255):
                    self.o.text_color = [255, 255, 255]
                if self.wordle.stats.state['p'] != (255, 255, 255):
                    self.p.text_color = [255, 255, 255]
                if self.wordle.stats.state['q'] != (255, 255, 255):
                    self.q.text_color = [255, 255, 255]
                if self.wordle.stats.state['r'] != (255, 255, 255):
                    self.r.text_color = [255, 255, 255]
                if self.wordle.stats.state['s'] != (255, 255, 255):
                    self.s.text_color = [255, 255, 255]
                if self.wordle.stats.state['t'] != (255, 255, 255):
                    self.t.text_color = [255, 255, 255]
                if self.wordle.stats.state['u'] != (255, 255, 255):
                    self.u.text_color = [255, 255, 255]
                if self.wordle.stats.state['v'] != (255, 255, 255):
                    self.v.text_color = [255, 255, 255]
                if self.wordle.stats.state['w'] != (255, 255, 255):
                    self.w.text_color = [255, 255, 255]
                if self.wordle.stats.state['x'] != (255, 255, 255):
                    self.x.text_color = [255, 255, 255]
                if self.wordle.stats.state['y'] != (255, 255, 255):
                    self.y.text_color = [255, 255, 255]
                if self.wordle.stats.state['z'] != (255, 255, 255):
                    self.z.text_color = [255, 255, 255]
                self.a.prep_msg(self.a.msg)
                self.b.prep_msg(self.b.msg)
                self.c.prep_msg(self.c.msg)
                self.d.prep_msg(self.d.msg)
                self.e.prep_msg(self.e.msg)
                self.f.prep_msg(self.f.msg)
                self.g.prep_msg(self.g.msg)
                self.h.prep_msg(self.h.msg)
                self.i.prep_msg(self.i.msg)
                self.j.prep_msg(self.j.msg)
                self.k.prep_msg(self.k.msg)
                self.l.prep_msg(self.l.msg)
                self.m.prep_msg(self.m.msg)
                self.n.prep_msg(self.n.msg)
                self.o.prep_msg(self.o.msg)
                self.p.prep_msg(self.p.msg)
                self.q.prep_msg(self.q.msg)
                self.r.prep_msg(self.r.msg)
                self.s.prep_msg(self.s.msg)
                self.t.prep_msg(self.t.msg)
                self.u.prep_msg(self.u.msg)
                self.v.prep_msg(self.v.msg)
                self.w.prep_msg(self.w.msg)
                self.x.prep_msg(self.x.msg)
                self.y.prep_msg(self.y.msg)
                self.z.prep_msg(self.z.msg)
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
                self.submit = buttons.Button(self.wordle, 655, 605, (125, 125, 125), "OK", 40, 40, (255, 255, 255))
                if (not self.wordle.stats.win) and (self.wordle.stats.round != 1) and (self.wordle.stats.round != 6 or not self.wordle.stats.win):
                    self.give = buttons.Button(self.wordle, 705, 605, (0, 139, 0), "?", 40, 40, (255, 255, 255))
                    self.give.draw_button()
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
                            c = (197, 180, 102)
                        else:
                            c = (125, 125, 125)
                        btn = buttons.Button(self.wordle, x + 5, y + 5, c, log_str[letter], 65, 65, (255, 255, 255))
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
                            c = (197, 180, 102)
                        else:
                            c = (125, 125, 125)
                        btn = buttons.Button(self.wordle, x + 5, y + 5, c, log_str[letter], 65, 65, (255, 255, 255))
                        btn.draw_button()
                        self.letters.append(btn)
                self.prnsc = buttons.Button(self.wordle, 800, 700, (197, 180, 102), "SAVE", 200, 100)
