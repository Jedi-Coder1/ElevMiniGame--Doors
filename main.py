import pyautogui as P
from time import sleep
from ahk import AHK


Y12 = 369
Y34 = 479
Y56 = 606
Y78 = 726
Y910 = 846
A = AHK()
P.FAILSAFE = False

while True:
    #1
    if P.locateCenterOnScreen('OneOn.png'):
        print('One Found')
        P.moveTo(737, Y12)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #2
    if P.locateCenterOnScreen('TwoOn.png'):
        print('Two Found')
        P.moveTo(974, Y12)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #3
    if P.locateCenterOnScreen('ThreeOn.png'):
        print('Three Found')
        P.moveTo(729, Y34)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #4
    if P.locateCenterOnScreen('FourOn.png'):
        print('Four Found')
        P.moveTo(970, Y34)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #5
    if P.locateCenterOnScreen('FiveOn.png'):
        print('Five Found')
        P.moveTo(730, Y56)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #6
    if P.locateCenterOnScreen('SixOn.png'):
        print('Six Found')
        P.moveTo(973, Y56)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #7
    if P.locateCenterOnScreen('SevenOn.png'):
        print('Seven Found')
        P.moveTo(732, Y78)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #8
    if P.locateCenterOnScreen('EightOn.png'):
        print('Eight Found')
        P.moveTo(976, Y78)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #9
    if P.locateCenterOnScreen('NineOn.png'):
        print('Nine Found')
        P.moveTo(734, Y910)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #10
    if P.locateCenterOnScreen('TenOn.png'):
        print('Ten Found')
        P.moveTo(974, Y910)
        sleep(0.1)
        A.click()
        sleep(0.5)