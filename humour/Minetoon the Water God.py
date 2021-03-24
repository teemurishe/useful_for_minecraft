import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 1
while count <= 30:
    pos = mc.player.getPos()
    mc.postToChat("Я Майнтун, Бог Воды Всего мира Майнкрафтового! Не подавали Вы жертв никаких столькие времена, да будьте же Вы прокляты на веки вечные! И да будет уроком это для Вас на времена бесконечные!")
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    count += 2
    time.sleep(1)
if count >= 30:
    mc.postToChat("И да будет для Вас сие проклятье уроком, да подавать вы жертвы не забывайте Богам всем великим, храм Богов Майнкрафтовских посещая...")
