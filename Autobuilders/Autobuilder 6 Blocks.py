from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103
def water():
    return 9
def bookshelf():
    return 47
def lava():
    return 11
def tnt():
    return 20
def poppy():
    return 38
def diamond():
    return 57

starter = input('Вы запустили программу "Автостроитель", часть 6: "Блоки". Желаете ли вы поставить какой-нибудь блок около себя? Да/Нет: ')
if starter == "Да": 
    chooser = input("Выберите блок: Арбуз/Вода/Полка/Лава/Динамит/Мак/Алмаз")
    if chooser == "Арбуз":
        block = melon()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Вода":
        block = water()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Полка":
        block = bookshelf()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Лава":
        block = lava()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Динамит":
        block = tnt()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Мак":
        block = poppy()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Алмаз":
        block = diamond()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    else:
      print("Введено некорректное имя блока. Программа остановлена. Пожалуйста, введите одно из предложенных наименований.")
      
elif starter == "Нет":
        print("Программа остановлена. Надеемся увидеть Вас снова!")
else:
    print("Некорректный ответ. Пожалуйста, введите один из предложенных вариантов. Программа остановлена.")
