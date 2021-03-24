from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 24
height = 10
levels = range(height)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for level in reversed(levels):
   mc.setBlocks(x - level, y, z - level, x + level, y, z + level,block)
   y += 1
