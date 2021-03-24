from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
pos = mc.player.getTilePos()
mc.postToChat(pos)
x = random.randint(1, 10000)
y = random.randint(50, 80)
z = random.randint(1, 10000)
mc.player.setPos(x, y, z)
posn = mc.player.getTilePos()
xb = posn.x
yb = posn.y
zb = posn.z
grass = 2
width = 3
height = 1
length = 3
mc.setBlocks(xb, yb, zb, xb+width-1, yb+height-1, zb+length-1, grass)
xn = xb+2
yn = yb+1
zn = zb+2
mc.player.setPos(xn, yn, zn)
posf = mc.player.getTilePos()
mc.postToChat(posf)
