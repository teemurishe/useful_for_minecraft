from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = int(input("X coordinate: "))
y = int(input("Y coordinate: "))
z = int(input("Z coordinate: "))
id = int(input("Block ID: "))
mc.setBlock(x,y,z, id)
