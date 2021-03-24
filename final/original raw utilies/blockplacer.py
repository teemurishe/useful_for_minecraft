from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = int(input("Координата по оси X: "))
y = int(input("Координата по оси Y: "))
z = int(input("Координата по оси Z: "))
id = int(input("ID блока: "))
mc.setBlock(x,y,z, id)