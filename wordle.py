import random
import sys
import time
from tkinter import messagebox
import pygame
import pygame.display
import pygame.event
import pygame.font
import pygame.time
import display
import library
import stats
pygame.init()
#TODO:定义游戏类
class Wordle:
    def __init__(self):
        """ Main class of game. """
        pygame.display.set_caption("Wordle")
        self.scr = pygame.display.set_mode((1000, 800))
        self.display = display.Display(self)
        self.stats = stats.Stats()
        self.library = library
        self.time = pygame.time.Clock()

    def run(self):
        """ Running the game. """
        while True:
            self.scr.fill((230, 230, 230))
            self._check_event()
            self.display.display()
            pygame.display.flip()

    def _check_event(self):
        """ Check the game event. """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.stats.mode == "ask":
                    for btn in self.display.buttons:
                        index = self.display.buttons.index(btn)
                        if btn.rect.collidepoint(pos):
                            if index == 8:
                                sys.exit()
                            else:
                                self.stats.letters = index + 4
                                self.stats.mode = "play"
                                lst = self.library.get_library_letter_num(self.stats.letters)
                                self.stats.answer = random.choice(lst)
                else:
                    if self.display.a.rect.collidepoint(pos):
                        self.stats.type_word += "a"
                    elif self.display.b.rect.collidepoint(pos):
                        self.stats.type_word += "b"
                    elif self.display.c.rect.collidepoint(pos):
                        self.stats.type_word += "c"
                    elif self.display.d.rect.collidepoint(pos):
                        self.stats.type_word += "d"
                    elif self.display.e.rect.collidepoint(pos):
                        self.stats.type_word += "e"
                    elif self.display.f.rect.collidepoint(pos):
                        self.stats.type_word += "f"
                    elif self.display.g.rect.collidepoint(pos):
                        self.stats.type_word += "g"
                    elif self.display.h.rect.collidepoint(pos):
                        self.stats.type_word += "h"
                    elif self.display.i.rect.collidepoint(pos):
                        self.stats.type_word += "i"
                    elif self.display.j.rect.collidepoint(pos):
                        self.stats.type_word += "j"
                    elif self.display.k.rect.collidepoint(pos):
                        self.stats.type_word += "k"
                    elif self.display.l.rect.collidepoint(pos):
                        self.stats.type_word += "l"
                    elif self.display.m.rect.collidepoint(pos):
                        self.stats.type_word += "m"
                    elif self.display.n.rect.collidepoint(pos):
                        self.stats.type_word += "n"
                    elif self.display.o.rect.collidepoint(pos):
                        self.stats.type_word += "o"
                    elif self.display.p.rect.collidepoint(pos):
                        self.stats.type_word += "p"
                    elif self.display.q.rect.collidepoint(pos):
                        self.stats.type_word += "q"
                    elif self.display.r.rect.collidepoint(pos):
                        self.stats.type_word += "r"
                    elif self.display.s.rect.collidepoint(pos):
                        self.stats.type_word += "s"
                    elif self.display.t.rect.collidepoint(pos):
                        self.stats.type_word += "t"
                    elif self.display.u.rect.collidepoint(pos):
                        self.stats.type_word += "u"
                    elif self.display.v.rect.collidepoint(pos):
                        self.stats.type_word += "v"
                    elif self.display.w.rect.collidepoint(pos):
                        self.stats.type_word += "w"
                    elif self.display.x.rect.collidepoint(pos):
                        self.stats.type_word += "x"
                    elif self.display.y.rect.collidepoint(pos):
                        self.stats.type_word += "y"
                    elif self.display.z.rect.collidepoint(pos):
                        self.stats.type_word += "z"
                    elif self.display.back.rect.collidepoint(pos):
                        self.stats.type_word = self.stats.type_word[0:-1]
                    elif self.display.submit.rect.collidepoint(pos):
                        self._check_answer()
                    if len(self.stats.type_word) > self.stats.letters:
                        self.stats.type_word = self.stats.type_word[0:self.stats.letters]
            elif event.type == pygame.KEYDOWN:
                if self.stats.mode == "ask":
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                else:
                    if event.key == pygame.K_ESCAPE:
                        self.stats.mode = "ask"
                        self.stats.__init__()
                    elif event.key == pygame.K_a:
                        self.stats.type_word += "a"
                    elif event.key == pygame.K_b:
                        self.stats.type_word += "b"
                    elif event.key == pygame.K_c:
                        self.stats.type_word += "c"
                    elif event.key == pygame.K_d:
                        self.stats.type_word += "d"
                    elif event.key == pygame.K_e:
                        self.stats.type_word += "e"
                    elif event.key == pygame.K_f:
                        self.stats.type_word += "f"
                    elif event.key == pygame.K_g:
                        self.stats.type_word += "g"
                    elif event.key == pygame.K_h:
                        self.stats.type_word += "h"
                    elif event.key == pygame.K_i:
                        self.stats.type_word += "i"
                    elif event.key == pygame.K_j:
                        self.stats.type_word += "j"
                    elif event.key == pygame.K_k:
                        self.stats.type_word += "k"
                    elif event.key == pygame.K_l:
                        self.stats.type_word += "l"
                    elif event.key == pygame.K_m:
                        self.stats.type_word += "m"
                    elif event.key == pygame.K_n:
                        self.stats.type_word += "n"
                    elif event.key == pygame.K_o:
                        self.stats.type_word += "o"
                    elif event.key == pygame.K_p:
                        self.stats.type_word += "p"
                    elif event.key == pygame.K_q:
                        self.stats.type_word += "q"
                    elif event.key == pygame.K_r:
                        self.stats.type_word += "r"
                    elif event.key == pygame.K_s:
                        self.stats.type_word += "s"
                    elif event.key == pygame.K_t:
                        self.stats.type_word += "t"
                    elif event.key == pygame.K_u:
                        self.stats.type_word += "u"
                    elif event.key == pygame.K_v:
                        self.stats.type_word += "v"
                    elif event.key == pygame.K_w:
                        self.stats.type_word += "w"
                    elif event.key == pygame.K_x:
                        self.stats.type_word += "x"
                    elif event.key == pygame.K_y:
                        self.stats.type_word += "y"
                    elif event.key == pygame.K_z:
                        self.stats.type_word += "z"
                    elif event.key == pygame.K_BACKSPACE:
                        self.stats.type_word = self.stats.type_word[0:-1]
                    elif event.key == pygame.K_RETURN:
                        self._check_answer()
                    if len(self.stats.type_word) > self.stats.letters:
                        self.stats.type_word = self.stats.type_word[0:self.stats.letters]
            elif event.type == pygame.QUIT:
                if self.stats.mode == "ask":
                    sys.exit()
                else:
                    self.stats.mode = "ask"
                    self.stats.__init__()
        
    def _check_answer(self):
        """ Check guess answer. """
        if self.stats.round < 6:
            if len(self.stats.type_word) != self.stats.letters:
                self._warning("Complete all leters! ")
            else:
                lst = self.library.get_library_letter_num(self.stats.letters)
                if not self.stats.type_word in lst:
                    self._warning("The word not in the list!")
                else:
                    pygame.display.set_caption("Wordle")
                    if self.stats.type_word == self.stats.answer:
                        colors = "ggggg"
                        self.stats.log.append(self.stats.type_word)
                        self.stats.colors.append(colors)
                        self.time.tick(500)
                        self.display.display()
                        self.time.tick(500)
                        self._info("Correct! ")
                    else:
                        colors = [" ", " ", " ", " "]
                        for _ in range(self.stats.letters - 4):
                            colors.append(" ")
                        green = []
                        grey = []
                        red = []
                        self.stats.reset_nums()
                        for idx, char in enumerate(self.stats.type_word):
                            if char == self.stats.answer[idx]:
                                green.append((char, idx))
                            elif char in self.stats.answer:
                                grey.append((char, idx))
                            else:
                                red.append((char, idx))
                        for char, idx in green:
                            self.stats.state[char] = (0, 255, 0)
                            self.stats.nums[char] += 1
                            colors[idx] = "g"
                        for char, idx in grey:
                            all = self.stats.answer.count(char)
                            if self.stats.nums[char] < all:
                                if not char in green:
                                    self.stats.state[char] = (255, 255, 0)
                                    colors[idx] = "y"
                                else:
                                    self.stats.state[char] = (0, 255, 0)
                                    colors[idx] = "y"
                            else:
                                self.stats.state[char] = (125, 125, 125)
                                colors[idx] = "b"
                            self.stats.nums[char] += 1
                        for char, idx in red:
                            if self.stats.state[char] != (0, 255, 0) or\
                                self.stats.state[char] != (255, 255, 0):
                                self.stats.state[char] = (125, 125, 125)
                            self.stats.nums[char] += 1
                            colors[idx] = "b"
                        cs = ''.join(colors)
                        self.stats.log.append(self.stats.type_word)
                        self.stats.colors.append(colors)
                        self.stats.type_word = ""
                        self.stats.round += 1
        else:
            if len(self.stats.type_word) != self.stats.letters:
                self._warning("Complete all letters! ")
            else:
                lst = self.library.get_library_letter_num(self.stats.letters)
                if not self.stats.type_word in lst:
                    self._warning("The word not in the list!")
                else:
                    pygame.display.set_caption("Wordle")
                    if self.stats.type_word == self.stats.answer:
                        colors = "ggggg"
                        self.stats.log.append(self.stats.type_word)
                        self.stats.colors.append(colors)
                        self.display.display()
                        self.time.tick(500)
                        self._info("Correct! ")
                    else:
                        colors = [" ", " ", " ", " "]
                        for _ in range(self.stats.letters - 4):
                            colors.append(" ")
                        self.stats.reset_nums()
                        green = []
                        grey = []
                        red = []
                        for idx, char in enumerate(self.stats.type_word):
                            if char == self.stats.answer[idx]:
                                green.append((char, idx))
                            elif char in self.stats.answer:
                                grey.append((char, idx))
                            else:
                                red.append((char, idx))
                        for char, idx in green:
                            self.stats.state[char] = (0, 255, 0)
                            self.stats.nums[char] += 1
                            colors[idx] = "g"
                        for char, idx in grey:
                            all = self.stats.answer.count(char)
                            if self.stats.nums[char] < all:
                                if not char in green:
                                    self.stats.state[char] = (255, 255, 0)
                                    colors[idx] = "y"
                                else:
                                    self.stats.state[char] = (0, 255, 0)
                                    colors[idx] = "y"
                            else:
                                self.stats.state[char] = (125, 125, 125)
                                colors[idx] = "b"
                            self.stats.nums[char] += 1
                        for char, idx in red:
                            if self.stats.state[char] != (0, 255, 0) or\
                                self.stats.state[char] != (255, 255, 0):
                                self.stats.state[char] = (125, 125, 125)
                            self.stats.nums[char] += 1
                            colors[idx] = "b"
                        cs = ''.join(colors)
                        self.stats.log.append(self.stats.type_word)
                        self.stats.colors.append(colors)
                        self._info("Correct answer: " + self.stats.answer)

    def _info(self, msg):
        self.stats.win = True
        pygame.display.set_caption(msg)
        self.time.tick(500)
        messagebox.showinfo(msg, msg)

    def _warning(self, msg):
        pygame.display.set_caption(msg)
        messagebox.showwarning(msg, msg)

#TODO:运行
if __name__ == '__main__':
    w = Wordle()
    w.run()
