import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
starter = input('"Autobuilder" started, part 7: "Blocks". Do you want
to continue? Yes/No: ')

if starter == "Да":
    pos = mc.player.getTilePos()
    x = pos.x + 1
    y = pos.y
    z = pos.z
    blocks = [20,20,20]
    lazuli = 22
    glass = 20
    count = 0
    mc.postToChat("Часы построены успешно! Они будут работать вечно, пока
    программа не будет остановлена...")
    while True:
        while count <= len(blocks):
           mc.setBlock(x, y , z, blocks[0])
           mc.setBlock(x, y + 1 , z, blocks[1])
           mc.setBlock(x, y + 2 , z, blocks[2])
           count += 1
           del blocks[-1]
           blocks.insert(0, lazuli)
           time.sleep(1)
        while count <= len(blocks):
           mc.setBlock(x, y + 2, z, blocks[0])
           mc.setBlock(x, y + 1 , z, blocks[1])
           mc.setBlock(x, y , z, blocks[2])
           count += 1
           del blocks[-1]
           blocks.insert(0, lazuli)
           time.sleep(1)


elif starter == "Нет":
    print("Программа остановлена. Надеемся увидеть Вас снова!")
else:
    print("Некорректный ответ. Пожалуйста, введите один из предложенных вариантов. Программа остановлена.")
