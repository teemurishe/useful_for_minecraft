from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    mc.setBlocks(x,y,z, x,y+7,z, 17)
    mc.setBlocks(x-3,y+8,z-3, x+3,y+8,z+3, 161)
    mc.setBlocks(x-2,y+9,z-2, x+2,y+9,z+2, 161)

starter = input('"Autobuilder" started, part 4: "Forest buider". Do you want
to continue? Yes/No: ')

if starter == "Yes":
    asker = ("Where do you want to build the house? Near/Far away: ")
    if asker == "Near":
        pos = mc.player.getTilePos()
        x = pos.x
        y = pos.y
        z = pos.z

        growTree(x + 1, y, z)
        growTree(x + 5, y, z)
        growTree(x + 1, y, z + 5)
        growTree(x + 5, y, z + 5)
        mc.postToChat("Forest built succesful! Thanks for using and hope to see
        you again!")
    elif asker == "Far away":
        x = input("X position: ")
        y = input("Y  position: ")
        z = input("Z  position: ")

        growTree(x + 1, y, z)
        growTree(x + 5, y, z)
        growTree(x + 1, y, z + 5)
        growTree(x + 5, y, z + 5)
        mc.postToChat("Forest built succesful! Thanks for using and hope to see
        you again!")
    else:
        print("Incorrect choice. Please, try again. Program stopped!")
elif starter == "No":
    print("Program stopped. Hope to see you again!")
else:
    print("Incorrect choice. Please, try again. Program stopped!")
