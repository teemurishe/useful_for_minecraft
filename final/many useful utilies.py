from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

print(
    'Добро пожаловать в набор утилит для строительства, перемещение, и многого другого в Майнкрафте! Пожалуйста, выберите утилиту из предложенного ниже списка:')

print('1. Поставка блока по Python-координатам')
print('2. Постройка рядом с собой плоской поверхности заданных размеров')
print('3. Возвращение на точку смерти')
print('4. Телепортация в рандомную точку мира')
print('5. Телепортер по системе Python')
print('6. ВЗРЫВАТЕЛЬ!!!')


def beginProgramm():
    pass


def blockSetter():
    x = int(input("Координата по оси X: "))
    y = int(input("Координата по оси Y: "))
    z = int(input("Координата по оси Z: "))
    id = int(input("ID блока: "))
    mc.setBlock(x, y, z, id)


def flatPattern():
    pos = mc.player.getTilePos()
    x, y, z = pos.x, pos.y, pos.z
    air, grass = 0, 2

    aw = int(input("Длина стороны плоскости: "))
    ah, al = 256, aw
    gw.gh, gl = al, 1, gw

    mc.setBlocks(x, y, z, x + aw, y + ah, z + al, air)
    mc.setBlocks(x, y, z, x + gw, y + gh, z + gl, grass)


def deathSaver():
    pos = mc.player.getTilePos()
    print('Точка телепортации: ' + str(pos))
    time.sleep(2)
    mc.player.setTilePos(pos)


def randTeport():
    pos = mc.player.getTilePos()
    mc.postToChat('Ваша текущая позиция: ' + str(pos))

    x = random.randint(1, 10000)
    y = random.randint(50, 80)
    z = random.randint(1, 10000)
    mc.player.setPos(x, y, z)

    posn = mc.player.getTilePos()
    xb, yb, zb = posn.x, posn.y, posn.z
    grass = 2
    width, height, length = 3, 1, 3
    mc.setBlocks(xb, yb, zb, xb + width - 1, yb + height - 1, zb + length - 1, grass)

    xn, yn, zn = xb + 2, yb + 1, zb + 2
    mc.player.setPos(xn, yn, zn)

    posf = mc.player.getTilePos()
    mc.postToChat('Ваша новая позиция по системе Python: ' + str(posf))


def pyTeleport():
    x = int(input("Координата по оси X: "))
    y = int(input("Координата по оси Y: "))
    z = int(input("Координата по оси Z: "))
    mc.player.setTilePos(x, y, z)


def tntSetter():
    mc.postToChat("Встаньте на точку, где желаете соверщить взрыв. Ваши координаты будут записаны через 5 секунд.")
    time.sleep(5)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    tnt = 46
    fire = 51
    mc.postToChat(
        "ВНИМАНИЕ!!! Чтобы избежать зависаний в игре, отлетите на примерно 20-50 блоков и наслаждайтесь зрелищем! Ваши координаты уже записаны, поэтому взрывной кубик появится там, где Вы стояли ранее :)")
    print(
        "ВНИМАНИЕ!!! Чтобы избежать зависаний в игре, отлетите на примерно 20-50 блоков и наслаждайтесь зрелищем! Ваши координаты уже записаны, поэтому взрывной кубик появится там, где Вы стояли ранее :)")
    w = int(input('Сторона взрывного кубика: '))
    h = w
    l = h
    mc.setBlocks(x, y, z, x + w, y + h, z + l, tnt)
    mc.setBlock(x + 1, y + 1, z + 1, fire)


while choice != 'Stop':
    choice = input('Выберите утилиту: ')
    print('Чтобы завершить работу с пакетом утилит, введите "Стоп"')

    if choice == '1':
        blockSetter()
    if choice == '2':
        flatPattern()
    if choice == '3':
        deathSaver()
    if choice == '4':
        randTeport()
    if choice == '5':
        pyTeleport()
    if choice == '6':
        tntSetter()
