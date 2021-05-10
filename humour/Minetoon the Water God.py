import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 1
while count <= 30:
    pos = mc.player.getPos()
    mc.postToChat("I am Minetoon, the Water God of Minecraft! I haven't seen\
    your toll for so long! You're cursed!")
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    count += 2
    time.sleep(1)
if count >= 30:
    mc.postToChat("This would be a lesson for you! Don't forget to give money\
    to great Gods of Minecraft!")
