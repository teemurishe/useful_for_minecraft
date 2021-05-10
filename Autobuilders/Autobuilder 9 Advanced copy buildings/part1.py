import shelve
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('"Autobuilder" started, part 9: "Advanced copy buildings". Do you want\
to continue? Yes/No: ')


def sortPair(val1, val2):
   if val1 > val2:
       return val2, val1
   else:
       return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
   x1, x2 = sortPair(x1, x2)
   y1, y2 = sortPair(y1, y2)
   z1, z2 = sortPair(z1, z2)
   width = x2 - x1
   height = y2 - y1
   length = z2 - z1
   structure = []
   print("Please, wait...")
   for row in range(height):
       structure.append([])
       for column in range(width):
           structure[row].append([])
           for depth in range(length):
               block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
               structure[row][column].append(block)
   return structure

input("Go to the first angle and press Enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Copying to file...")
structure = copyStructure(x1, y1, z1, x2, y2, z2)

structureName = input("Name the building: ")

shelveFile = shelve.open("shelveFile.db")
shelveFile[structureName] = structure1
shelveFile.close()

input("Go to the first angle and press Enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Copying to file...")
structure = copyStructure(x1, y1, z1, x2, y2, z2)

structureName = input("Name the building: ")

shelveFile = shelve.open("shelveFile.db")
shelveFile[structureName] = structure2
shelveFile.close()

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Name the building: ")
structure = copyStructure(x1, y1, z1, x2, y2, z2)

structureName = input("Name the building: ")

shelveFile = shelve.open("shelveFile.db")
shelveFile[structureName] = structure3
shelveFile.close()

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Go to the second angle and press Enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

print("Copying to file...")
structure = copyStructure(x1, y1, z1, x2, y2, z2)

structureName = input("Name the building: ")

shelveFile = shelve.open("shelveFile.db")
shelveFile[structureName] = structure4
shelveFile.close()

print("Program stopped. Please, open the next part of Autobuilder.")
