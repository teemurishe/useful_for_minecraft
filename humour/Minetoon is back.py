import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

mc.postToChat("Me, The God of water, Minetoon is here again! Where are your money?!
 Stupid human, now you won't walk comfortably!")
while True:
   mc.setBlock(x, y, z, 38.0)
   x += random.uniform(-0.2, 0.2)
   z += random.uniform(-0.2, 0.2)
   y = mc.getHeight(x, z)
   mc.player.setPos(x, y, z)
   time.sleep(0.1)
