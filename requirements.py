""" Install requirements. """
#TODO:安装第三方库
import os
import lists
for r in lists.THIRD_PARTIES:
    os.system("pip3 install {r}")
