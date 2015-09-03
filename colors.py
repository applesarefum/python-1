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

y    ="\033[0;33m"
o    ="\033[1;31m"
r    ="\033[0;31m"
m    ="\033[0;35m"
v    ="\033[1;35m"
b    ="\033[0;34m"
c    ="\033[0;36m"
g    ="\033[0;32m"
b03  ="\033[1;30m"
b02  ="\033[0;30m"
b01  ="\033[1;32m"
b00  ="\033[1;33m"
b0   ="\033[1;34m"
b1   ="\033[1;36m"
b2   ="\033[0;37m"
b3   ="\033[1;37m"
re   ="\033[0m"
cl   ="\033[H\033[2J"

import random
colors=[y,o,r,m,v,b,c,g]
bases=[b02,b01,b00,b0,b1,b2,b3]
def rc():
    return random.choice(colors)

if __name__=="__main__":
    print(y+'Yellow '+o+'Orange '+r+'Red '+m+'Magenta '+v+'Violet '+b+'Blue '+c+'Cyan '+g+'Green')
    print(b03+'base03 '+b02+'base02 '+b01+'base01 '+b00+'base00 '+b0+'base0 '+b1+'base1 '+b2+'base2 '+b3+'base3')
    for count in range(5):
        color1=rc()
        color2=rc()
        color3=rc()
        print(color1+'lel '+color2+'sweg '+color3+'XD',end=' ')
    print(r)
