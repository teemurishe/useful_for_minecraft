from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z
 
file = open('10.txt', 'r', encoding='utf-8')
 
for line in file:
    data = line.split(',')
    x = pos.x + 1
    for block in data:
        mc.setBlock(x, y, z, int(block))
        mc.setBlock(x, y+1, z, int(block))
        mc.setBlock(x, y+2, z, int(block))
        x = x + 1
    z = z + 1
