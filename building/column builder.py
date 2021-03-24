from mcpi.minecraft import minecraft
mc = minecraft.create()
import time

pos = mc.player.getTilePos
x = pos.x
y = pos.y
z = pos.z

blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
lazuli = 22

def build_column():
    count = 0
    while count < len(blocks):
        mc.etBlock(x, y + count, z, blocs(count))

count = 0
while count < len(blocks):
    mc.setBlock(x, y + count, z, blocs[count])
    count = count + 1
count = 0
while count < len(blocks):
    del blocks[-1]
    block.insert(0, lazuli)
