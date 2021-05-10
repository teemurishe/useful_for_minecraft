from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

not_a_diamond = 10
answer = input("Congratulations! Cheat activated! Do you want to continue?\
(Yes/No): ")
mc.postToChat("Congratulations! Cheat activated! Do you want to continue?\
(Yes/No) Use Python Console to contiue")

if answer == "Yes":
    print("WARNING!!! To proceed, please, turn off other cheats!")
    mc.postToChat("WARNING!!! To proceed, please, turn off other cheats!")
    w = int(input("Enter width of diamond ore: "))
    h = int(input("Enter height of diamond ore: "))
    l = int(input("Enter length of diamond ore: "))
    mc.setBlocks(x, y, z, x+w, y+h, z+l, not_a_diamond)
    mc.postToChat("Are you stupid?..")
elif answer == "No":
    print("Congratulations, you are not stupid! To proceed acceptance to\
    programmists of Minecraft transfer 1 dollar to 4817 7602 2418 2786 card")
else:
    print("Incorrect choice. Please, try again. Program stopped!")
