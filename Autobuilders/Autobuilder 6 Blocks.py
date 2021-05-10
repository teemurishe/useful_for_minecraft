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

starter = input('"Autobuilder" started, part 6: "Blocks". Do you want\
to continue? Yes/No: ')
if starter == "Да":
    chooser = input("Choose block: Watermelon/Water/Shelf/Lava/TNT/Poppy/Diamond")
    if chooser == "Watermelon":
        block = melon()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Water":
        block = water()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Shelf":
        block = bookshelf()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Lava":
        block = lava()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "TNT":
        block = tnt()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Poppy":
        block = poppy()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    elif chooser == "Diamond":
        block = diamond()
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y, pos.z, block)
    else:
      print("Incorrect choice. Please, try again. Program stopped!")

elif starter == "Нет":
        print("Program stopped. Hope to see you again!")
else:
    print("Incorrect choice. Please, try again. Program stopped!")
