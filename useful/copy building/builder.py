import pickle
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('Вы запустили программу "Автостроитель", часть 10: "Копир строений". Желаете ли вы прочитать здание из файла? Да/Нет: ')
fileName = input('Введите имя файла с раширением, в который записано строение: ')

def buildStructure(x, y, z, structure):
   xStart = x
   zStart = z
   for row in structure:
       for column in row:
           for block in column:
               mc.setBlock(x, y, z, block.id, block.data)
               z += 1
           x += 1
           z = zStart
       y += 1
       x = xStart

pickleFile = open(str(filename), "rb")
structure = pickle.load(pickleFile)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, structure)
pickleFile.close()

print("Программа остановлена. Благодарим Вас за использование юбилейного выпуска Автостроителя и ждём Вас снова!")
