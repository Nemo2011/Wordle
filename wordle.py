""" Main program. """
import random
import sys
import time
import pygame
import answer
import buttons
import display
import hard
import imagesave
import library
import message
import stats
import textcopy
pygame.init()
__version__  = 5.0
__date__ = "2022-2-20"
#TODO:定义游戏类
class Wordle:
    def __init__(self):
        """ Main class of game. """
        pygame.display.set_caption("Wordle")
        self.scr = pygame.display.set_mode((1000, 650))
        self.display = display.Display(self)
        self.stats = stats.Stats()
        self.library = library
        self.message = message.Message(self)

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
                            if index == 5:
                                sys.exit()
                            elif index == 7:
                                self.message._info(f"Wordle {str(__version__)}, {__date__}, Python, by YiMoXia, <yimoxia@outlook.com>")
                                self.display.display()
                            elif index == 4:
                                self.stats.easy = False
                            elif index == 3:
                                self.stats.easy = True
                            elif index == 6:
                                going = True
                                while going:
                                    btn0 = buttons.Button(self, 0, 0, (255, 255, 255), "How to play?", 1000, 100)
                                    btn1 = buttons.Button(self, 0, 100, (230, 230, 230), "1. Open and choose your level. ", 1000, 50)
                                    btn2 = buttons.Button(self, 0, 150, (255, 255, 255), "2. Hard mode: Green letters must stay fixed, yellow letters must be reused. ", 1000, 50)
                                    btn3 = buttons.Button(self, 0, 200, (230, 230, 230), "3. You need to guess a word. Use keyboard or mouse to type-in your guess. ", 1000, 50)
                                    btn4 = buttons.Button(self, 0, 250, (255, 255, 255), "4. You have 6 turns to guess. ", 1000, 50)
                                    btn5 = buttons.Button(self, 0, 300, (0, 139, 0), "5. Green means the letter in the correct place. ", 1000, 50)
                                    btn6 = buttons.Button(self, 0, 350, (255, 255, 0), "6. Yellow means the letter in the word but not the correct place.", 1000, 50)
                                    btn7 = buttons.Button(self, 0, 400, (125, 125, 125), "7. Grey means this letter not in the word or there are no any this letter. ", 1000, 50)
                                    btn8 = buttons.Button(self, 0, 450, (230, 230, 230), "8. You can click red 'x' to back to the setting page. ", 1000, 50)
                                    btn9 = buttons.Button(self, 0, 500, (255, 255, 255), "9. Copy emoji or download picture after the game.", 1000, 50)
                                    btn10 = buttons.Button(self, 0, 550, (230, 230, 230), "10. Click red 'x' or click ESC in the level-choose page to exit.", 1000, 50)
                                    ok = buttons.Button(self, 0, 600, (0, 0, 255), "OK", 1000, 50, (255, 255, 255))
                                    btn0.draw_button()
                                    btn1.draw_button()
                                    btn2.draw_button()
                                    btn3.draw_button()
                                    btn4.draw_button()
                                    btn5.draw_button()
                                    btn6.draw_button()
                                    btn7.draw_button()
                                    btn8.draw_button()
                                    btn9.draw_button()
                                    btn10.draw_button()
                                    ok.draw_button()
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            pos = pygame.mouse.get_pos()
                                            if ok.rect.collidepoint(pos):
                                                going = False
                                        elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                                                going = False
                                        elif event.type == pygame.QUIT:
                                            going = False
                            else:
                                self.stats.letters = index + 4
                                self.stats.mode = "play"
                                self.stats.answer = answer.get_answer_letter_num(self.stats.letters)                
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
                    if self.stats.cc:
                        if self.display.cc.rect.collidepoint(pos):
                            c = textcopy.Copy(self)
                            c.copy()
                        elif self.display.si.rect.collidepoint(pos):
                            i = imagesave.ImageSave(self)
                            i.save()
                    if (not self.wordle.stats.win) and (self.wordle.stats.round != 1) and (self.wordle.stats.round != 6 or not self.wordle.stats.win):
                        if self.display.give.rect.collidepoint(pos):
                            self.stats.type_word = self.stats.answer
                            self.stats.log.append(self.stats.type_word.upper())
                            self.stats.colors.append("g" * self.stats.letters)
                            self.stats.win = True
                            self.stats.cc = True
                            self.display.display()
                            pygame.display.flip()
                            self.message._warning(f"You lost! Correct answer: {self.stats.answer}")
            elif event.type == pygame.KEYDOWN:
                if self.stats.mode == "ask":
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                else:
                    if event.key == pygame.K_ESCAPE:
                        self.stats.mode = "ask"
                        self.stats.reset()
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
                    self.stats.reset()
        
    def _check_answer(self):
        """ Check guess answer. """
        if self.stats.round < 6:
            if len(self.stats.type_word) != self.stats.letters:
                self.display.display()
                pygame.display.flip()
                self.message._warning("Complete all leters! ")
            else:
                lst = self.library.get_library_letter_num(self.stats.letters)
                if not self.stats.type_word in lst:
                    self.display.display()
                    pygame.display.flip()
                    self.message._warning("The word not in the list!")
                else:
                    if ((not self.stats.easy) and hard.hard_valid(self, self.stats.type_word) == True) or self.stats.easy or self.stats.round == 1:
                        pygame.display.set_caption("Wordle")
                        if self.stats.type_word == self.stats.answer:
                            colors = "g" * self.stats.letters
                            self.stats.log.append(self.stats.type_word.upper())
                            self.stats.colors.append(colors)
                            self.stats.win = True
                            self.display.display()
                            pygame.display.flip()
                            self.message._info("The answer was correct! ")
                            self.stats.cc = True
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
                                self.stats.state[char] = (0, 139, 0)
                                self.stats.nums[char] += 1
                                colors[idx] = "g"
                            for char, idx in grey:
                                all = self.stats.answer.count(char)
                                if self.stats.nums[char] < all:
                                    if not self.stats.state[char] == (0, 139, 0):
                                        self.stats.state[char] = (255, 255, 0)
                                        colors[idx] = "y"
                                    else:
                                        self.stats.state[char] = (0, 139, 0)
                                        colors[idx] = "y"
                                else:
                                    if (not self.stats.state[char] == (0, 139, 0)) and (not self.stats.state[char] == (255, 255, 0)):
                                        self.stats.state[char] = (125, 125, 125)
                                    colors[idx] = "b"
                                self.stats.nums[char] += 1
                            for char, idx in red:
                                if (not self.stats.state[char] == (0, 139, 0)) and (not self.stats.state[char] == (255, 255, 0)):
                                    self.stats.state[char] = (125, 125, 125)
                                self.stats.nums[char] += 1
                                colors[idx] = "b"
                            cs = ''.join(colors)
                            self.stats.log.append(self.stats.type_word.upper())
                            self.stats.colors.append(colors)
                            self.stats.type_word = ""
                            self.stats.round += 1
                    else:
                        self.display.display()
                        pygame.display.flip()
                        self.message._warning(hard.hard_valid(self, self.stats.type_word)[1])
        else:
            if len(self.stats.type_word) != self.stats.letters:
                self.display.display()
                pygame.display.flip()
                self.message._warning("Complete all letters! ")
            else:
                lst = self.library.get_library_letter_num(self.stats.letters)
                if not self.stats.type_word in lst:
                    self.display.display()
                    pygame.display.flip()
                    self.message._warning("The word not in the list!")
                else:
                    if ((not self.stats.easy) and hard.hard_valid(self, self.stats.type_word) == True and self.stats.round != 1) or self.stats.easy:
                        pygame.display.set_caption("Wordle")
                        if self.stats.type_word == self.stats.answer:
                            colors = "g" * self.stats.letters
                            self.stats.log.append(self.stats.type_word.upper())
                            self.stats.colors.append(colors)
                            self.display.display()
                            pygame.display.flip()
                            self.message._info("The answer was correct! ")
                            self.stats.cc = True
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
                                self.stats.state[char] = (0, 139, 0)
                                self.stats.nums[char] += 1
                                colors[idx] = "g"
                            for char, idx in grey:
                                all = self.stats.answer.count(char)
                                if self.stats.nums[char] < all:
                                    if not self.stats.state[char] == (0, 139, 0):
                                        self.stats.state[char] = (255, 255, 0)
                                        colors[idx] = "y"
                                    else:
                                        self.stats.state[char] = (0, 139, 0)
                                        colors[idx] = "y"
                                else:
                                    if (not self.stats.state[char] == (0, 139, 0)) and (not self.stats.state[char] == (255, 255, 0)):
                                        self.stats.state[char] = (125, 125, 125)
                                    colors[idx] = "b"
                                self.stats.nums[char] += 1
                            for char, idx in red:
                                if (not self.stats.state[char] == (0, 139, 0)) and (not self.stats.state[char] == (255, 255, 0)):
                                    self.stats.state[char] = (125, 125, 125)
                                self.stats.nums[char] += 1
                                colors[idx] = "b"
                            cs = ''.join(colors)
                            self.stats.log.append(self.stats.type_word.upper())
                            self.stats.colors.append(colors)
                            self.stats.win = True
                            self.display.display()
                            pygame.display.flip()
                            self.message._info("You lost! The correct answer is: " + self.stats.answer)
                            self.stats.cc = True
                    else:
                        self.display.display()
                        pygame.display.flip()
                        self.message._warning(hard.hard_valid(self, self.stats.type_word)[1])

#TODO:运行
if __name__ == '__main__':
    w = Wordle()
    w.run()
