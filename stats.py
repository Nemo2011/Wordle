""" Game stats class. """
#TODO:类定义
class Stats():
    def __init__(self):
        """ Game stat class. """
        self.mode = "ask"#or "play"
        self.answer = ""
        self.letters = 4
        self.state = {"a":(255, 255, 255), "b":(255, 255, 255), "c":(255, 255, 255), "d":(255, 255, 255), "e":(255, 255, 255), "f":(255, 255, 255), "g":(255, 255, 255), 
                      "h":(255, 255, 255), "i":(255, 255, 255), "j":(255, 255, 255), "k":(255, 255, 255), "l":(255, 255, 255), "m":(255, 255, 255), "n":(255, 255, 255), 
                      "o":(255, 255, 255), "p":(255, 255, 255), "q":(255, 255, 255), "r":(255, 255, 255), "s":(255, 255, 255), "t":(255, 255, 255), "u":(255, 255, 255), 
                      "v":(255, 255, 255), "w":(255, 255, 255), "x":(255, 255, 255), "y":(255, 255, 255), "z":(255, 255, 255)
        }
        self.round = 1
        self.type_word = ""
        self.log = []
        self.colors = []
