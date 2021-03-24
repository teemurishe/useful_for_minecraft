from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('"Autobuilder" started, part 8: "Stairs". Do you want
to continue? Yes/No: ')

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

stairBlock = 53

step = 0
for step in range(10):
    mc.setBlock(x + step, y + step, z, stairBlock, 1)
    mc.setBlock(x - step, y + step, z, stairBlock, 2)
    mc.setBlock(x, y + step, z + step, stairBlock, 3)
    mc.setBlock(x, y + step, z - step, stairBlock, 4)
mc.postToChat("4 stairs built succesful! Hope to see you again!")
print("Program stopped. Hope to see you again!")
