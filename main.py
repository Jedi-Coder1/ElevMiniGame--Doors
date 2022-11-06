import pydirectinput as Dir
import pyautogui as P
from time import sleep
from ahk import AHK


Y12 = 369
Y34 = 479
Y56 = 606
Y78 = 726
Y910 = 846
A = AHK()
confidence = 0.9
region = (2000,0,1000,1100)
P.FAILSAFE = False


while True:
    #1
    if P.locateOnScreen('OneOn.png', confidence=confidence, region = region):
        print('One Found')
        Dir.moveTo(737, Y12)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #2
    if P.locateOnScreen('TwoOn.png', confidence=confidence, region = region):
        print('Two Found')
        Dir.moveTo(974, Y12)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #3
    if P.locateOnScreen('ThreeOn.png', confidence=confidence, region = region):
        print('Three Found')
        Dir.moveTo(729, Y34)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #4
    if P.locateOnScreen('FourOn.png', confidence=confidence, region = region):
        print('Four Found')
        Dir.moveTo(970, Y34)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #5
    if P.locateOnScreen('FiveOn.png', confidence=confidence, region = region):
        print('Five Found')
        Dir.moveTo(730, Y56)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #6
    if P.locateOnScreen('SixOn.png', confidence=confidence, region = region):
        print('Six Found')
        Dir.moveTo(973, Y56)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #7
    if P.locateOnScreen('SevenOn.png', confidence=confidence, region = region):
        print('Seven Found')
        Dir.moveTo(732, Y78)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #8
    if P.locateOnScreen('EightOn.png', confidence=confidence, region = region):
        print('Eight Found')
        Dir.moveTo(976, Y78)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #9
    if P.locateOnScreen('NineOn.png', confidence=confidence, region = region):
        print('Nine Found')
        Dir.moveTo(734, Y910)
        sleep(0.1)
        A.click()
        sleep(0.5)
    #10
    if P.locateOnScreen('TenOn.png', confidence=confidence, region = region):
        print('Ten Found')
        Dir.moveTo(974, Y910)
        sleep(0.1)
        A.click()
        sleep(0.5)