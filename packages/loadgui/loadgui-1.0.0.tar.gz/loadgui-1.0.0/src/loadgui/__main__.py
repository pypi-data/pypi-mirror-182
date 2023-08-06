import time
import oscheck as oc

# Make this compatible with Windows XP - 11
oc.update_OS("Windows")
oc.update_OS_versions(vers = ["XP", "Vista", "7", "8", "10", "11"])
import platform
from os import system

__version__ = "1.0.0"
__os__  = oc.os()
__info__ = 0

def __main__():
    if oc.osCheck() and __info__:
        print("OS compatible with library.")
    if not oc.osCheck():
        if __info__:
            print("Sorry, your OS cannot run this.\n")
        incompatibleOS = "Your OS, \"" + platform.system() + " " + platform.release() + "\" does not match the OS \"" + __os__ + "\""
        raise Exception(incompatibleOS)

def __change_opposite__(var):
    change = var + " = 1 - " + var
    eval(change)

# Run an OS check
#try:
__change_opposite__("__info__")
#except SyntaxError:
#__info__ = 1 - __info__

__main__()

def exitcode():
    system("exit")

# This is where loading screen actually happens.
class Load:
    add_delay_time: int
    text: str

    def __init__(self, add_delay_time: int, text: str):
        self.add_delay_time = add_delay_time
        self.text = text

    def clear(self):
        system("cls")
        print(self.text)

    def load_right(self, delay: int):
        i = 0
        char = '_'
        while i != 9:
            i = i + 1
            self.clear()
            print(char * i)
            time.sleep(delay + self.add_delay_time)
    
    def load_down(self, delay: int):
        i = 0
        char = '|'
        while i != 3:
            i = i + 1
            print("\t" + char)
            time.sleep(delay + self.add_delay_time)
    
    def load_left(self, delay: int):
        i = 0
        char = '_'
        schar = '|'
        mc = ' '
        bc = """_________
        |
        |"""
        while i != 8:
            self.clear()
            print(bc)
            i = i + 1
            print(mc * (8 - i) + (char * i) + schar)
            time.sleep(delay + self.add_delay_time)
    
    def load_up(self, delay: int):
        i = 0
        char = '|'
        schar = '_'
        mc = "\n        " + char
        smc = "\n" + char + "       " + char
        tmc = "\n" + char + (schar * 7) + char
        fmc = "\n" + "↑       " + char
        bc = (schar * 9)
        while i != 3:
            self.clear()
            i = i + 1
            if i != 3:
                print(bc + (mc * (3 - i)) + (fmc * (i - 2)) + (smc * (i - 1)) + tmc)
            else:
                print(bc + (mc * (3 - i)) + (fmc * (i - 2)) + (smc * (i - 2)) + tmc)
            time.sleep(delay + self.add_delay_time)

# Define a function for users to execute for showing the loading screen
def load_screen(r, d, l, u, xdelay, xtext):
    __main__()
    load = Load(float(xdelay), str(xtext))
    load.load_right(float(r))
    load.load_down(float(d))
    load.load_left(float(l))
    load.load_up(float(u))
