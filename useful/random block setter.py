from mcpi.minecraft import minecraft
mc = minecraft.create()

pos = mc.player.getTilePos
x = pos.x
y = pos.y
z = pos.z

blocks = [57, 41, 56, 12, 64, 36, 46, 133, 3, 166]

block = random.choice(blocks)
mc.setBlock(x, y, z, block)
