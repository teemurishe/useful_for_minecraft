from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()

starter = input('"Autobuilder" started, part 2: "Spinning stairs". Do you want\
to continue? Yes/No: ')

if starter == "Yes":
    print("Please, stand where you want to build stairs. You have 5 seconds\
    before your position would be recorded.")
    time.sleep(5)
    x = pos.x
    y = pos.y
    z = pos.z
    print("Position recorded succesful! Please, wait...")
    time.sleep(2)
    mc.setBlock(x, y, z+1, 109)
    turner = input("Stairs built succesful! Do you want to spin it? Yes/No: ")
    if turner == "Yes":
        mc.setBlock(x, y, z + 1, 109, True)
        print("Program stopped. Hope to see you again!")
    if turner =="No":
        print("Program stopped. Hope to see you again!")
if starter == "No":
    print("Program stopped. Hope to see you again!")
