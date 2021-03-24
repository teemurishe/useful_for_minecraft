from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

count = 1
time = int(input("Time if working: "))
block = int(input("Block ID: "))
air = 0
while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    below = mc.getBlock(x, y - 1, z)
    if below != air:
        mc.setBlock(x, y, z, block)
