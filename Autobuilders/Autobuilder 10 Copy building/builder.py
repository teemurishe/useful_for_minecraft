import pickle
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('"Autobuilder" started, part 10: "Copy buildings". Do you want\
to continue? Yes/No: ')
fileName = input('Enter the name of the file with buildings: ')

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

print("Program stopped. Hope to see you again!")
