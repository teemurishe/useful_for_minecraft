from mcpi.minecraft import Minecraft
mc = Minecraft.create()

try:
    x = int(input("X position: "))
    y = int(input("Y position: "))
    z = int(input("Z position: "))
    block = int(input("Block ID: "))
    w = int(input("Length of side of cube: "))
    h = w
    l = h
    mc.player.setPos(x, y, z)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x, y, z, x + w, y + h, z + l, block)
except:
    mc.postToChat("One of the values are entered incorrectly. Please, try again")
    print("One of the values are entered incorrectly. Please, try again")
