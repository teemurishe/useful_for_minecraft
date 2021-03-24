from mcpi.minecraft import Minecraft
import time
 
mc = Minecraft.create()
 
count = 1
time = int(input("Время действия: "))
block = int(input("ID блока: "))
air = 0
while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    below = mc.getBlock(x, y - 1, z)
    if below != air:
        mc.setBlock(x, y, z, block)
#mineberg максим цвеиков гриферит
