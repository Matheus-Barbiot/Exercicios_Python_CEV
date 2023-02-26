from time import sleep
from emoji import emojize

for n in range (10, 0, -1):
    print (n)
    sleep (1)

print (emojize('\033[36mKABOOM ZOOM BUUUM\033[m :party_popper:'))