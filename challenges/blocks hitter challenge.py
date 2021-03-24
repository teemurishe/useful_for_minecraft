import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(60)

hits = mc.events.pollBlockHits()
block = 103
mc.postToChat("Добро пожаловать в новую мини-игру на время! Ваша цель - в течение ровно 1 минуты ударить как можно больше блоков! Затем, телепортируясь, вы узнаете, сколько блоков ударили! Поехали чрез 5, 4, 3...")
time.sleep(5)
for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.player.setPos(x,y,z)
    time.sleep(10)
mc.postToChat("Итак, вы ударили ровно" + str(len(hits)) + "раз!")
if len(hits) < 30:
    mc.postToChat("Что ж, это не так уж и много, но для первого раза вполне неплохо! Вот тебе приз :)")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 42)
if len(hits) < 10:
    mc.postToChat("Не, ну ты и...! СГОРИ В АДУ!!!")
    mc.setBlock(pos.x, pos.y, pos.z, 90)
if len(hits) < 50:
    mc.postToChat("Вау, да ты, видимо, переиграл в куки-кликер! АЛМАЗЫ В СТУДИЮ!!!")
    mc.setBlock(pos.x, pos.y, pos.z, 57)
    mc.setBlock(pos.x, pos.y + 1, pos.z, 57)
if len(hits) < 80:
    mc.postToChat("МАКРОСЫ ВЫРУБИЛ!!! На тебе энд, давай, помакроси тут с драконом...")
    mc.setBlock(pos.x, pos.y, pos.z, 119)
print("Программа остановлена. Благодарим за использование и ждём Вас снова!")
