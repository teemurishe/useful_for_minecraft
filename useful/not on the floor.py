from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock (x-1, y-1, z-1)

mc.postToChat("The player is flying or jumping: " + str(blockType == 0))
