from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

blockAbove = mc.getBlock(x,y+2,z)
blockUnder = mc.getBlock(x,y-1,z)

inTunnel = blockUnder != 0 and blockAbove != 0

mc.postToChat("Игрок в туннеле: " + str(inTunnel))