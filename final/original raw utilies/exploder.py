from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
mc.postToChat("Get to the explosion position. 5 seconds to position getting...")
print("Get to the explosion position. 5 seconds to position getting...")
time.sleep(5)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
tnt = 46
fire = 51
mc.postToChat("WARNING!!! To avoid bugs, get away on 20-50 blocks and enjoy the sight! Your position is got succesful :)")
print("WARNING!!! To avoid bugs, get away on 20-50 blocks and enjoy the sight! Your position is got succesful :)")
w = int(input('Explosing cube\'s side length: '))
h = w
l = h
mc.setBlocks(x, y, z, x+w, y+h, z+l, tnt)
mc.setBlock(x+1, y+1, z+1, fire)
