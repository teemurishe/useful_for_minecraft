from mcpi.minecraft import Minecraft
mc = Minecraft.create()

starter = input('"Autobuilder" started, part 1: "Box-like house". Do you want\
to continue? Yes/No: ')

if starter == "Yes":
    place = input("Where do you want to build the house? Near/Far away: ")
    if place == "Near":
        print("The house will be built near you right now! Please wait...")
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
    if place == "Far away":
        print("The house will be built on the points you should enter right now.")
        print('WARNING! You should use the Python numbering system!')
        x = int(input("X position: "))
        y = int(input("Y position: "))
        z = int(input("Z position: "))
        stone = 1
        air = 0
        w = 5
        h = w
        l = h
        mc.setBlocks(x, y, z, x + w, y + h, z + l, stone)
        mc.setBlocks(x + 1, y + 1, z + 1, x + w - 1, y + h - 1, z + l - 1, air)
        mc.setBlocks(x, y, z, x + w, y + h + 3, z + l, air)
if starter == "No":
    print("Program stopped. Hope to see you again!")
