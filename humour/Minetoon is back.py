import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

mc.postToChat("И снова к вам явился я, Майнкрафта бог воды и льда, Майнтун зовёте вы меня! Опять вы дани, люди, не приносите, за что регулярно наказание поносите! Узри ж мою мощь, и не ходи ты больше ровно, человечишко жалкий!")
while True:
   mc.setBlock(x, y, z, 38.0)
   x += random.uniform(-0.2, 0.2)
   z += random.uniform(-0.2, 0.2)
   y = mc.getHeight(x, z)
   mc.player.setPos(x, y, z)
   time.sleep(0.1)