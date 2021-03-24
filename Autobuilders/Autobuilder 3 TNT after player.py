import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

starter = input('"Autobuilder" started, part 3: "TNT road". Do you want
to continue? Yes/No: ')

if starter == "Yes":
    print("Please, stand where you want to start the road. It would be built
    behind you. 15 seconds left to the beginning!")
    print('To stop this, just close Python console.')
    time.sleep(15)
    while True:
        pos = mc.player.getPos()
        mc.setBlock(pos.x, pos.y, pos.z, 46)
        time.sleep(0.2)
if starter == "No":
    print("Program stopped. Hope to see you again!")
