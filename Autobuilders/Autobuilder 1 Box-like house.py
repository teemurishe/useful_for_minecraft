from mcpi.minecraft import Minecraft
mc = Minecraft.create()

starter = input('Вы запустили программу "Автостроитель", часть 1: "Дом-коробка". Желаете ли вы построить основу для дома? Да/Нет: ')

if starter == "Да":
    place = input("Желаете ли Вы построить дом возле себя или в другой точке? Рядом/Далеко: ")
    if place == "Рядом":
        print("Дом будет построен рядом с Вами. Ожидайте!")
        pos = mc.player.getTilePos()
        x = pos.x
        y = pos.y
        z = pos.z
        stone = 1
        air = 0
        w = 5
        h = w
        l = h
        mc.setBlocks(x, y, z, x + w, y + h, z + l, stone)
        mc.setBlocks(x + 1, y + 1, z + 1, x + w -1, y + h - 1, z + l - 1, air)
        mc.setBlocks(x + 1, y + 1, z + 1, 0)
    if place == "Далеко":
        print("Дом будет построен по координатам, которые Вы введёте далее. ВНИМАНИЕ!!! Координаты необходимо ввести по системе исчисления Python!")
        x = int(input("Введите координату по оси X: "))
        y = int(input("Введите координату по оси Y: "))
        z = int(input("Введите координату по оси Z: "))
        stone = 1
        air = 0
        w = 5
        h = w
        l = h
        mc.setBlocks(x, y, z, x + w, y + h, z + l, stone)
        mc.setBlocks(x + 1, y + 1, z + 1, x + w - 1, y + h - 1, z + l - 1, air)
        mc.setBlocks(x, y, z, x + w, y + h + 3, z + l, air)
if starter == "Нет":
    print("Программа остановлена. Надеемся увидеть Вас снова!")
