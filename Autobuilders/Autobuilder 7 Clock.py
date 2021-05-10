import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
starter = input('"Autobuilder" started, part 7: "Clock". Do you want\
to continue? Yes/No: ')

if starter == "Yes":
    pos = mc.player.getTilePos()
    x = pos.x + 1
    y = pos.y
    z = pos.z
    blocks = [20,20,20]
    lazuli = 22
    glass = 20
    count = 0
    mc.postToChat("Clock built succesful! To stop them, close Python interpreter")
    while True:
        while count <= len(blocks):
           mc.setBlock(x, y , z, blocks[0])
           mc.setBlock(x, y + 1 , z, blocks[1])
           mc.setBlock(x, y + 2 , z, blocks[2])
           count += 1
           del blocks[-1]
           blocks.insert(0, lazuli)
           time.sleep(1)
        while count <= len(blocks):
           mc.setBlock(x, y + 2, z, blocks[0])
           mc.setBlock(x, y + 1 , z, blocks[1])
           mc.setBlock(x, y , z, blocks[2])
           count += 1
           del blocks[-1]
           blocks.insert(0, lazuli)
           time.sleep(1)


elif starter == "No":
    print("Program stopped. Hope to see you again!")
else:
    print("Incorrect choice. Please, try again. Program stopped!")
