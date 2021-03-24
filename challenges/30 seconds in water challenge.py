import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('Приветствуем в челлендже "Продержись под водой 30 секунд!" Цель челленджа - продержаться под водой 30 секунд! За определённые промежутки времени под водой вы будете получать награды. Когда будете готовы, напишите "Начать", чтобы начать выполнение челленджа')
starter = input("Ожидание команды начала... ")
score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    mc.postToChat("Текущий счет: " + str(score))
mc.postToChat("Окончательный счет: " + str(score))
if score > 15:
    mc.postToChat("Поздравляем! Вы продержались под водой уже целых 15 секунд!")
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
if score > 20:
    pos = mc.player.getTilePos
    mc.setBlock(pos.x, pos.y, pos.z, 41)
    mc.postToChat("Поразительно! Вы смогли продержаться под водой уже 20 секунд!")
if score > 30:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 264)
    mc.postToChat("Поздравляем! Вы выполнили этот челлендж! Пройдя через такие старания, вы заслуживаете АЛМАЗОВ!!!")
    
