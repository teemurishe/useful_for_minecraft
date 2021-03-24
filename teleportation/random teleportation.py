from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

pos = mc.player.getTilePos()
mc.postToChat("Your position at the moment:")
mc.postToChat(pos)
mc.postToChat("5 second to teleportation...")
time.sleep(5)

x = random.randint(1, 10000)
y =random.randint(60, 80)
z =random.randint(1, 10000)
mc.player.setPos(x, y, z)

posn = mc.player.getTilePos()
xb = posn.x
yb = posn.y
zb = posn.z

grass = 2
dandelion = 37

width = 3
height = 1
length = 3

mc.setBlocks(xb, yb, zb, xb+width-1, yb+height-1, zb+length-1, grass)
mc.setBlocks(xb, yb+1, zb, xb+width, yb+height, zb+length, dandelion)

xn = xb+2
yn = yb+1
zn = zb+2
mc.player.setPos(xn, yn, zn)

mc.postToChat("Teleportation succesful! Your new position:")
posf = mc.player.getTilePos()
mc.postToChat(posf)
