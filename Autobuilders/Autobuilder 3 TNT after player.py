import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

starter = input('Вы запустили программу "Автостроитель", часть 3: "Путевой взрыватель". Желаете ли вы построить дорогу из динамита за собой? Да/Нет: ')

if starter == "Да":
    print("Встаньте в точку, где Вы начнёте Вашу взрывную дорогу. За Вами после каждого шага будет строиться динамитная дорога. Осталось 15 секунд до начала постройки. Для остановки закройте программу.")
    time.sleep(15)
    while True:
        pos = mc.player.getPos()
        mc.setBlock(pos.x, pos.y, pos.z, 46)
        time.sleep(0.2)
if starter == "Нет":
    print("Программа остановлена. Надеемся увидеть Вас снова!")
