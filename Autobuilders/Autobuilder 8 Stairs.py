from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('Вы запустили программу "Автостроитель", часть 8: "Лестницы". Желаете ли вы построить несколько лестниц около себя? Да/Нет: ')

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

stairBlock = 53

step = 0
for step in range(10):
    mc.setBlock(x + step, y + step, z, stairBlock, 1)
    mc.setBlock(x - step, y + step, z, stairBlock, 2)
    mc.setBlock(x, y + step, z + step, stairBlock, 3)
    mc.setBlock(x, y + step, z - step, stairBlock, 4)
mc.postToChat("4 лестницы построены успешно! Благодарим за использование и ждём Вас снова!")
print("Программа остановлена. Надеемся увидеть Вас снова!")
