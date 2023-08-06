'''                                                   
  cccc yy   yy   aa aa nn nnn  rr rr    aa aa zzzzz   eee  
cc     yy   yy  aa aaa nnn  nn rrr  r  aa aaa   zz  ee   e 
cc      yyyyyy aa  aaa nn   nn rr     aa  aaa  zz   eeeee  
 ccccc      yy  aaa aa nn   nn rr      aaa aa zzzzz  eeeee 
        yyyyy                                              
        made by @cyanraze
        https://github.com/CodeIntelligenceAgency
        https://cia.works
'''
from os import system

def grellow(text):
    system(""); output = ""
    red = 250
    for line in text.splitlines():
        output += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
        if not red == 0:
            red -= 70
            if red < 70:
                red = 200
    return output

def green_flames(text):
    system(""); output = ""
    green = 111
    for line in text.splitlines():
        output += (f"\033[38;2;100;{green};1m{line}\033[0m\n")
        if not green == 255:
            green += 20
            if green > 255:
                green = 255
    return output

def crimson(text):
    system(""); output = ""
    red = 22
    for line in text.splitlines():
        output += (f"\033[38;2;{red};48;43m{line}\033[0m\n")
        if not red == 0:
            red -= 10
            if red < 70:
                red = 200
    return output

def flaming(text):
    system(""); output = ""
    green = 115
    for line in text.splitlines():
        output += (f"\033[38;2;234;{green};23m{line}\033[0m\n")
        if not green == 255:
            green += 10
            if green > 255:
                green = 255
    return output

def purplish(text):
    system(""); output = ""
    green = 10
    for line in text.splitlines():
        output += (f"\033[38;2;100;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return output

def pink(text):
    system(""); output = ""
    green = 10
    for line in text.splitlines():
        output += (f"\033[38;2;250;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return output