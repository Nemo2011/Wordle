""" Save image for the game result. """
from tkinter import filedialog
import pygame
import buttons
import message
#TODO:定义类
class ImageSave:
    def __init__(self, wordle):
        """ Save result with image. """
        self.wordle = wordle
        self.message = message.Message(self.wordle)

    def save(self):
        """ Save image. """
        new_rct = pygame.Rect(0, 0, 1000, 500)
        new_sur = pygame.Surface((1000, 500))
        self.wordle.display.display()
        new_sur.blit(self.wordle.scr, new_rct)
        local = ""
        going = True
        cancel = False
        while going:
            btn = buttons.Button(self.wordle, 300, 150, (0, 0, 255), "Type-in the location: ", 400, 100)
            t1 = buttons.Button(self.wordle, 0, 400, (255, 255, 255), r"You can type in ':' with key [;], '\' and '/' with [/] and [\].", 1000, 50)
            t2 = buttons.Button(self.wordle, 0, 450, (255, 255, 255), "You can type in lower letters. Upper letters use [SHIFT]. EG:[u]+[SHIFT]=[U].", 1000, 50)
            t3 = buttons.Button(self.wordle, 0, 500, (255, 255, 255), "You can use [BACKSPACE] and [ENTER]. ", 1000, 50)
            btn.draw_button()
            t1.draw_button()
            t2.draw_button()
            t3.draw_button()
            ok = buttons.Button(self.wordle, 300, 350, (0, 255, 0), "OK", 200, 50)
            ok.draw_button()
            c = buttons.Button(self.wordle, 500, 350, (125, 125, 125), "CANCEL", 200, 50)
            c.draw_button()
            inputbox = buttons.Button(self.wordle, 0, 250, (255, 255, 255), local, 1000, 100)
            inputbox.draw_button()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        local += "a"
                    elif event.key == pygame.K_b:
                        local += "b"
                    elif event.key == pygame.K_c:
                        local += "c"
                    elif event.key == pygame.K_d:
                        local += "d"
                    elif event.key == pygame.K_e:
                        local += "e"
                    elif event.key == pygame.K_f:
                        local += "f"
                    elif event.key == pygame.K_g:
                        local += "g"
                    elif event.key == pygame.K_h:
                        local += "h"
                    elif event.key == pygame.K_i:
                        local += "i"
                    elif event.key == pygame.K_j:
                        local += "j"
                    elif event.key == pygame.K_k:
                        local += "k"
                    elif event.key == pygame.K_l:
                        local += "l"
                    elif event.key == pygame.K_m:
                        local += "m"
                    elif event.key == pygame.K_n:
                        local += "n"
                    elif event.key == pygame.K_o:
                        local += "o"
                    elif event.key == pygame.K_p:
                        local += "p"
                    elif event.key == pygame.K_q:
                        local += "q"
                    elif event.key == pygame.K_r:
                        local += "r"
                    elif event.key == pygame.K_s:
                        local += "s"
                    elif event.key == pygame.K_t:
                        local += "t"
                    elif event.key == pygame.K_u:
                        local += "u"
                    elif event.key == pygame.K_v:
                        local += "v"
                    elif event.key == pygame.K_w:
                        local += "w"
                    elif event.key == pygame.K_x:
                        local += "x"
                    elif event.key == pygame.K_y:
                        local += "y"
                    elif event.key == pygame.K_z:
                        local += "z"
                    elif event.key == pygame.K_BACKSLASH:
                        local += "\\"
                    elif event.key == pygame.K_SLASH:
                        local += "/"
                    elif event.key == pygame.K_SEMICOLON:
                        local += ":"
                    elif event.key == pygame.K_PERIOD:
                        local += "."
                    elif event.key == pygame.K_BACKSPACE:
                        if len(local) != 0:
                            local = local[0:-1]
                    elif event.key == pygame.K_RETURN:
                        going = False
                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if len(local) != 0:
                            last = local[-1]
                            local = local[0:-1] + last.upper()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ok.rect.collidepoint(pos):
                        going = False
                    elif c.rect.collidepoint(pos):
                        cancel = True
                        going = False
        if not cancel:
            try:
                pygame.image.save(new_sur, local)
                self.message._info("Saved successfully! ")
            except:
                self.message._warning("Error. Please try again. ")
        self.wordle.display.display()
        pygame.display.flip()
