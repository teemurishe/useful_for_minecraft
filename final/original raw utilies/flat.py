from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
air = 0
grass = 2
aw = int(input("Flat area's side length: "))
ah = 15
al = aw
gw = al
gh = 1
gl = gw
mc.setBlocks(x, y, z, x+aw, y+ah, z+al, air)
mc.setBlocks(x, y, z, x+gw, y+gh, z+gl, grass)
