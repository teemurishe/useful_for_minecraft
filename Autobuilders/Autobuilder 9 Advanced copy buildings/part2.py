import shelve
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('"Autobuilder" started, part 9: "Advanced copy buildings". Do you want\
to continue? Yes/No: ')


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

structureDictionary = shelve.open("shelveFile.db")

structureName = input("Name of the building: ")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, structureDictionary[structureName])

print("Program stopped. Hope to see you again!")
