"""Colors Module

lol, rainbowz
"""

yellow  ="\033[0;33m"
orange  ="\033[1;31m"
red     ="\033[0;31m"
magenta ="\033[0;35m"
violet  ="\033[1;35m"
blue    ="\033[0;34m"
cyan    ="\033[0;36m"
green   ="\033[0;32m"
base03  ="\033[1;30m"
base02  ="\033[0;30m"
base01  ="\033[1;32m"
base00  ="\033[1;33m"
base0   ="\033[1;34m"
base1   ="\033[1;36m"
base2   ="\033[0;37m"
base3   ="\033[1;37m"
reset   ="\033[0m"
clear   ="\033[H\033[2J"

import random
colors=[yellow,orange,red,magenta,violet,blue,cyan,green]
bases=[base02,base01,base00,base0,base1,base2,base3]
def random_color():
    return random.choice(colors)
def random_base():
    return random.choice(base)

if __name__=="__main__":
    print(yellow+'Yellow '+orange+'Orange '+red+'Red '+magenta+'Magenta '+violet+'Violet '+blue+'Blue '+cyan+'Cyan '+green+'Green')
    input(base03+'base03 '+base02+'base02 '+base01+'base01 '+base00+'base00 '+base0+'base0 '+base1+'base1 '+base2+'base2 '+base3+'base3')
    print(clear)
    for count in range(111):
        color1=random_color()
        color2=random_color()
        color3=random_color()
        print(color1+'lel '+color2+'sweg '+color3+'XD',end=' ')
    print(reset)
