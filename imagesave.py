""" Save image for the game result. """
import os
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
        left = True
        while going:
            btn = buttons.Button(self.wordle, 200, 0, (0, 0, 255), "Choose an location to save: ", 600, 150, (0, 0, 0))
            t1 = buttons.Button(self.wordle, 0, 350, (255, 255, 255), r"You can type in ':', '/', '\', '.', '-', '='", 1000, 50)
            t2 = buttons.Button(self.wordle, 0, 400, (125, 125, 125), " Upper letters use [SHIFT]. EG:[u]+[SHIFT]=[U].", 1000, 50, (255, 255, 255))
            t3 = buttons.Button(self.wordle, 0, 450, (255, 255, 255), "[-] + [SHIFT] = [_], [=] + [SHIFT] = [+]. ", 1000, 50)
            t4 = buttons.Button(self.wordle, 0, 500, (125, 125, 125), "[9] + [SHIFT] = [(], [0] + [SHIFT] = [)]. ", 1000, 50, (255, 255, 255))
            t5 = buttons.Button(self.wordle, 0, 550, (255, 255, 255), "You can use [BACKSPACE] and [ENTER]. ", 1000, 50)
            t6 = buttons.Button(self.wordle, 0, 600, (125, 125, 125), "Please type [SHIFT] first. ", 1000, 50, (255, 255, 255))
            btn.draw_button()
            t1.draw_button()
            t2.draw_button()
            t3.draw_button()
            t4.draw_button()
            t5.draw_button()
            t6.draw_button()
            if left:
                ok = buttons.Button(self.wordle, 0, 300, (0, 255, 0), "OK", 500, 50)
                ok.draw_button()
                c = buttons.Button(self.wordle, 500, 300, (125, 125, 125), "CANCEL", 500, 50)
                c.draw_button()
            else:
                ok = buttons.Button(self.wordle, 0, 300, (125, 125, 125), "OK", 500, 50)
                ok.draw_button()
                c = buttons.Button(self.wordle, 500, 300, (0, 255, 0), "CANCEL", 500, 50)
                c.draw_button()
            inputbox = buttons.Button(self.wordle, 0, 150, (255, 255, 255), local, 1000, 150)
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
                    elif event.key == pygame.K_MINUS:
                        local += "-"
                    elif event.key == pygame.K_EQUALS:
                        local += "="
                    elif event.key == pygame.K_0:
                        local += "0"
                    elif event.key == pygame.K_8:
                        local += "8"
                    elif event.key == pygame.K_9:
                        local += "9"
                    elif event.key == pygame.K_1:
                        local += "1"
                    elif event.key == pygame.K_2:
                        local += "2"
                    elif event.key == pygame.K_3:
                        local += "3"
                    elif event.key == pygame.K_4:
                        local += "4"
                    elif event.key == pygame.K_5:
                        local += "5"
                    elif event.key == pygame.K_6:
                        local += "6"
                    elif event.key == pygame.K_7:
                        local += "7"
                    elif event.key == pygame.K_BACKSPACE:
                        if len(local) != 0:
                            local = local[0:-1]
                    elif event.key == pygame.K_ESCAPE:
                        cancel = True
                        going = False
                    elif event.key == pygame.K_RETURN:
                        if not left:
                            cancel = True
                        going = False
                    elif event.key == pygame.K_LEFT:
                        if not left:
                            left = True
                    elif event.key == pygame.K_RIGHT:
                        if left:
                            left = False
                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        if len(local) != 0:
                            last = local[-1]
                            if last == last.upper():
                                if last == "9":
                                    local = local[0:-1] + "("
                                elif last == "0":
                                    local = local[0:-1] + ")"
                                elif last == "-":
                                    local = local[0:-1] + "_"
                                elif last == "=":
                                    local = local[0:-1] + "+"
                            else:
                                local = local[0:-1] + last.upper()        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ok.rect.collidepoint(pos):
                        left = True
                        going = False
                    elif c.rect.collidepoint(pos):
                        left = False
                        cancel = True
                        going = False
                elif event.type == pygame.QUIT:
                    cancel = True
                    going = False
        if left:
            ok = buttons.Button(self.wordle, 0, 300, (0, 255, 0), "OK", 500, 50)
            ok.draw_button()
            c = buttons.Button(self.wordle, 500, 300, (125, 125, 125), "CANCEL", 500, 50)
            c.draw_button()
        else:
            ok = buttons.Button(self.wordle, 0, 300, (125, 125, 125), "OK", 500, 50)
            ok.draw_button()
            c = buttons.Button(self.wordle, 500, 300, (0, 255, 0), "CANCEL", 500, 50)
            c.draw_button()
        pygame.display.flip()
        if not cancel:
            try:
                if local.count("/") != 0:
                    name = local.split("/")[-1]
                    length = len(name)
                    folder = local[0:len(local) - length]
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                elif local.count("\\") != 0:
                    name = local.split(r"\\")[-1]
                    length = len(name)
                    folder = local[0:len(local) - length]
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                pygame.image.save(new_sur, local)
            except:
                self.message._warning("Error. Please try again. ")     
            else:
                self.message._info("Successfully to save the image. ")           
        self.wordle.display.display()
        pygame.display.flip()
