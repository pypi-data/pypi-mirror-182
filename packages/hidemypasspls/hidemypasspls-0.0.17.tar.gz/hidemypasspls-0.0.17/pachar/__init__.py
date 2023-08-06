import os
import sys
try:
    import msvcrt
except:
    pass
try:
    import getch
except:
    pass
import shutil


from time import sleep
from setuptools import setup, Extension



RETURN = []
Black= "\u001b[30m"
Red= "\u001b[31m"
Green= "\u001b[32m"
Yellow= "\u001b[33m"
Blue= "\u001b[34m"
Magenta= "\u001b[35m"
Cyan= "\u001b[36m"
White= "\u001b[37m"
Reset= "\u001b[0m"

COLORLIST = ["\u001b[30m","\u001b[31m","\u001b[32m","\u001b[33m","\u001b[34m","\u001b[35m","\u001b[36m","\u001b[37m","\u001b[0m"]


WordLIST = []


def INPUT(text,x,y,NOENTER=False, NPRINT=False):
    try:
        WordLIST.clear()
    except:
        pass
    OS = os.name
    if OS == "nt":
        #posix
        #nt
        print(text, end='')
        sys.stdout.write('\r' + (' ' * shutil.get_terminal_size()[0]))
        print ("\033[A")
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y, f"{text}"))
        sys.stdout.flush()
        #f = open("keys.txt", "a")
        while True:
            #f = open("keys.txt", "a")
            PRINT = False
            if msvcrt.kbhit():
                key = (str(msvcrt.getch()))
                s = key.replace('b', '', 1)
                d = s.replace("'", "")
                if d == Fr'\x9c':
                    pass
                    #f.write(u"\xa3")
                elif d == 'Â':
                    pass
                elif d == Fr'\r':
                    pass
                else:
                    WordLIST.append(F"{d}")
                if PRINT == True:
                    print(d)
                    break
                PRINT = True
                # box = F'''
                # ╔═╗
                # ║{d}║
                # ╚═╝'''
                if d == r"\r":
                    pass
                else:
                    pass
                if d == r"\x08":
                    sys.stdout.write('\r' + (' ' * shutil.get_terminal_size()[0]))
                    print ("\033[A")
                    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y, f"{text}"))
                    sys.stdout.flush()
                    WordLIST.clear()
                elif NOENTER == True:
                    if d == r"\r":
                        pass
                    else:
                        WordLIST.append(F"{d}")
                elif d == r"\r":
                    print("                             \033[A")
                    break
                else:
                    if NPRINT == True:
                        sys.stdout.write(F"{text}")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y+2, f"{text}"))
                        sys.stdout.flush()
                        #print(F"{d}", end = '')
                        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (14, 4+1, f"\r"))
                        sys.stdout.flush()
    elif OS == "posix":
        print(text, end='')
        sys.stdout.write('\r' + (' ' * shutil.get_terminal_size()[0]))
        print ("\033[A")
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y, f"{text}"))
        sys.stdout.flush()
        while True:
            PRINT = False
            key = getch.getch()
            try:
                ESCCODES = ord(key)
            except:
                pass
            if ESCCODES == 10:
                break
            elif ESCCODES == 127:
                sys.stdout.write('\r' + (' ' * shutil.get_terminal_size()[0]))
                print ("\033[A")
                sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y, f"{text}"))
                sys.stdout.flush()
                WordLIST.clear()
            else:
                pass
            if key == Fr'\x9c':
                try:
                    WordLIST.append(u"\xa3")
                except:
                    pass
            elif key == 'Â':
                pass
            else:
                try:
                    WordLIST.append(F"{key}")
                except:
                    pass
            PRINT = True
            # box = F'''
            # ╔═╗
            # ║{d}║
            # ╚═╝'''
            if key == r"\r":
                pass
            else:
                pass
            if key == r"\x08":
                sys.stdout.write('\r' + (' ' * shutil.get_terminal_size()[0]))
                print ("\033[A")
                sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y, f"{text}"))
                sys.stdout.flush()
                WordLIST.clear()
            elif NOENTER == True:
                if key == r"\r":
                    pass
                else:
                    WordLIST.append(F"{key}")
            elif key == r"\r":
                print("                             \033[A")
                break
            else:
                if NPRINT == True:
                    sys.stdout.write(F"{text}")
                    sys.stdout.flush()
                else:
                    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x,y+2, f"{text}"))
                    sys.stdout.flush()
                    #print(F"{d}", end = '')
                    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (14, 4+1, f"\r"))
                    sys.stdout.flush()
    else:
        print("Unsupported OS!")



def READ():
    global userinput
    WordString = ''.join(map(str, WordLIST))
    READ.userinput = WordString
    #print("\n"+READ.userinput)


def RAINBOW(x,y,Loop=False):
    if Loop==True:
        while True:
            for i in COLORLIST:
                sleep(0.5)
                sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, F"{i}Some shit"))
                sys.stdout.flush()
    elif Loop==False:
        for i in COLORLIST:
            sleep(0.5)
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, F"{i}Some shit"))
            sys.stdout.flush()
    else:
        print(F"{White}There was an error! Please pick Loops={Red}False{White}/{Green}True{White} or {Green}1/{Red}2{White}")