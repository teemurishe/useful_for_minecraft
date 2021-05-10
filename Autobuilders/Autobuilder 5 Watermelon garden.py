import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def makeMelon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y - 1, z, 103)

starter = input('"Autobuilder" started, part 5: "Watermelon garden". Do you want\
to continue? Yes/No: ')
if starter == "Yes":
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    mc.postToChat("Garden built succesful! Hope to see you again!")
if starter == "Нет":
    print("Program stopped. Hope to see you again!")
else:
    print("Incorrect choice. Please, try again. Program stopped!")
