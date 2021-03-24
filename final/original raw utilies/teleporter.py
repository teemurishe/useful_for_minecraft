from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = int(input("Координата по оси X: "))
y = int(input("Координата по оси Y: "))
z = int(input("Координата по оси Z: "))
mc.player.setTilePos(x, y, z)