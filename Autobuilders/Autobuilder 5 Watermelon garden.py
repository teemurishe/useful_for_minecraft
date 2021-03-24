import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def makeMelon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y - 1, z, 103)

starter = input('Вы запустили программу "Автостроитель", часть 5: "Арбузная грядка". Желаете ли вы построить небольшую грядку арбузов около себя? Да/Нет: ')
if starter == "Да":
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    time.sleep(10)
    makeMelon()
    mc.postToChat("Грядка построена рядом с Вами! Благодарим за использование программы и надеемся увидеть Вас снова!")
if starter == "Нет":
    print("Программа остановлена. Надеемся увидеть Вас снова!")
else:
    print("Некорректный ответ. Пожалуйста, введите один из предложенных вариантов. Программа остановлена.")
