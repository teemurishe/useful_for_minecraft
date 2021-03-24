import time
from mcpi.minecraft import Minecraft
import minecraftstuff as mcstuff

mc = Minecraft.create()

rocketPos = mc.player.getTilePos()
rocketPos.z = rocketPos.z + 1
rocketPos.y = rocketPos.y + 1

blockSetter = mcstuff.MinecraftShape(mc, rocketPos)
lava = 11
ironBlock = 42

blockSetter.setBlock(-2,0,0,lava)
blockSetter.setBlock(-3,0,0,lava)
blockSetter.setBlock(-4,0,0,lava)
blockSetter.setBlock(-5,0,0,lava)
blockSetter.setBlock(-6,0,0,lava)
blockSetter.setBlock(-7,0,0,lava)
blockSetter.setBlock(-8,0,0,lava)
blockSetter.setBlock(-9,0,0,lava)
blockSetter.setBlock(2,0,0,lava)
blockSetter.setBlock(3,0,0,lava)
blockSetter.setBlock(4,0,0,lava)
blockSetter.setBlock(5,0,0,lava)
blockSetter.setBlock(6,0,0,lava)
blockSetter.setBlock(7,0,0,lava)
blockSetter.setBlock(8,0,0,lava)
blockSetter.setBlock(9,0,0,lava)
blockSetter.setBlock(-2,1,0,lava)
blockSetter.setBlock(-3,1,0,lava)
blockSetter.setBlock(-4,1,0,lava)
blockSetter.setBlock(-5,1,0,lava)
blockSetter.setBlock(-6,1,0,lava)
blockSetter.setBlock(-7,1,0,lava)
blockSetter.setBlock(-8,1,0,lava)
blockSetter.setBlock(-9,1,0,lava)
blockSetter.setBlock(2,1,0,lava)
blockSetter.setBlock(3,1,0,lava)
blockSetter.setBlock(4,1,0,lava)
blockSetter.setBlock(5,1,0,lava)
blockSetter.setBlock(6,1,0,lava)
blockSetter.setBlock(7,1,0,lava)
blockSetter.setBlock(8,1,0,lava)
blockSetter.setBlock(9,1,0,lava)
blockSetter.setBlock(-2,2,0,lava)
blockSetter.setBlock(-3,2,0,lava)
blockSetter.setBlock(-4,2,0,lava)
blockSetter.setBlock(-5,2,0,lava)
blockSetter.setBlock(-6,2,0,lava)
blockSetter.setBlock(-7,2,0,lava)
blockSetter.setBlock(-8,2,0,lava)
blockSetter.setBlock(-9,2,0,lava)
blockSetter.setBlock(2,2,0,lava)
blockSetter.setBlock(3,2,0,lava)
blockSetter.setBlock(4,2,0,lava)
blockSetter.setBlock(5,2,0,lava)
blockSetter.setBlock(6,2,0,lava)
blockSetter.setBlock(7,2,0,lava)
blockSetter.setBlock(8,2,0,lava)
blockSetter.setBlock(9,2,0,lava)
blockSetter.setBlock(-2,3,0,lava)
blockSetter.setBlock(-3,3,0,lava)
blockSetter.setBlock(-4,3,0,lava)
blockSetter.setBlock(-5,3,0,lava)
blockSetter.setBlock(-6,3,0,lava)
blockSetter.setBlock(-7,3,0,lava)
blockSetter.setBlock(-8,3,0,lava)
blockSetter.setBlock(-9,3,0,lava)
blockSetter.setBlock(2,3,0,lava)
blockSetter.setBlock(3,3,0,lava)
blockSetter.setBlock(4,3,0,lava)
blockSetter.setBlock(5,3,0,lava)
blockSetter.setBlock(6,3,0,lava)
blockSetter.setBlock(7,3,0,lava)
blockSetter.setBlock(8,3,0,lava)
blockSetter.setBlock(9,3,0,lava)
blockSetter.setBlock(-2,4,0,lava)
blockSetter.setBlock(-3,4,0,lava)
blockSetter.setBlock(-4,4,0,lava)
blockSetter.setBlock(-5,4,0,lava)
blockSetter.setBlock(-6,4,0,lava)
blockSetter.setBlock(-7,4,0,lava)
blockSetter.setBlock(-8,4,0,lava)
blockSetter.setBlock(-9,4,0,lava)
blockSetter.setBlock(2,4,0,lava)
blockSetter.setBlock(3,4,0,lava)
blockSetter.setBlock(4,4,0,lava)
blockSetter.setBlock(5,4,0,lava)
blockSetter.setBlock(6,4,0,lava)
blockSetter.setBlock(7,4,0,lava)
blockSetter.setBlock(8,4,0,lava)
blockSetter.setBlock(9,4,0,lava)
blockSetter.setBlock(-2,5,0,lava)
blockSetter.setBlock(-3,5,0,lava)
blockSetter.setBlock(-4,5,0,lava)
blockSetter.setBlock(-5,5,0,lava)
blockSetter.setBlock(-6,5,0,lava)
blockSetter.setBlock(-7,5,0,lava)
blockSetter.setBlock(-8,5,0,lava)
blockSetter.setBlock(-9,5,0,lava)
blockSetter.setBlock(2,5,0,lava)
blockSetter.setBlock(3,5,0,lava)
blockSetter.setBlock(4,5,0,lava)
blockSetter.setBlock(5,5,0,lava)
blockSetter.setBlock(6,5,0,lava)
blockSetter.setBlock(7,5,0,lava)
blockSetter.setBlock(8,5,0,lava)
blockSetter.setBlock(9,5,0,lava)
blockSetter.setBlock(-2,6,0,lava)
blockSetter.setBlock(-3,6,0,lava)
blockSetter.setBlock(-4,6,0,lava)
blockSetter.setBlock(-5,6,0,lava)
blockSetter.setBlock(-6,6,0,lava)
blockSetter.setBlock(-7,6,0,lava)
blockSetter.setBlock(-8,6,0,lava)
blockSetter.setBlock(-9,6,0,lava)
blockSetter.setBlock(2,6,0,lava)
blockSetter.setBlock(3,6,0,lava)
blockSetter.setBlock(4,6,0,lava)
blockSetter.setBlock(5,6,0,lava)
blockSetter.setBlock(6,6,0,lava)
blockSetter.setBlock(7,6,0,lava)
blockSetter.setBlock(8,6,0,lava)
blockSetter.setBlock(9,6,0,lava)
blockSetter.setBlock(-2,7,0,lava)
blockSetter.setBlock(-3,7,0,lava)
blockSetter.setBlock(-4,7,0,lava)
blockSetter.setBlock(-5,7,0,lava)
blockSetter.setBlock(-6,7,0,lava)
blockSetter.setBlock(-7,7,0,lava)
blockSetter.setBlock(-8,7,0,lava)
blockSetter.setBlock(-9,7,0,lava)
blockSetter.setBlock(2,7,0,lava)
blockSetter.setBlock(3,7,0,lava)
blockSetter.setBlock(4,7,0,lava)
blockSetter.setBlock(5,7,0,lava)
blockSetter.setBlock(6,7,0,lava)
blockSetter.setBlock(7,7,0,lava)
blockSetter.setBlock(8,7,0,lava)
blockSetter.setBlock(9,7,0,lava)
blockSetter.setBlock(-2,8,0,lava)
blockSetter.setBlock(-3,8,0,lava)
blockSetter.setBlock(-4,8,0,lava)
blockSetter.setBlock(-5,8,0,lava)
blockSetter.setBlock(-6,8,0,lava)
blockSetter.setBlock(-7,8,0,lava)
blockSetter.setBlock(-8,8,0,lava)
blockSetter.setBlock(-9,8,0,lava)
blockSetter.setBlock(2,8,0,lava)
blockSetter.setBlock(3,8,0,lava)
blockSetter.setBlock(4,8,0,lava)
blockSetter.setBlock(5,8,0,lava)
blockSetter.setBlock(6,8,0,lava)
blockSetter.setBlock(7,8,0,lava)
blockSetter.setBlock(8,8,0,lava)
blockSetter.setBlock(9,8,0,lava)
blockSetter.setBlock(-3,9,0,ironBlock)
blockSetter.setBlock(-4,9,0,ironBlock)
blockSetter.setBlock(-5,9,0,ironBlock)
blockSetter.setBlock(-6,9,0,ironBlock)
blockSetter.setBlock(-7,9,0,ironBlock)
blockSetter.setBlock(3,9,0,ironBlock)
blockSetter.setBlock(4,9,0,ironBlock)
blockSetter.setBlock(5,9,0,ironBlock)
blockSetter.setBlock(6,9,0,ironBlock)
blockSetter.setBlock(7,9,0,ironBlock)
blockSetter.setBlock(-3,10,0,ironBlock)
blockSetter.setBlock(-4,10,0,ironBlock)
blockSetter.setBlock(-5,10,0,ironBlock)
blockSetter.setBlock(-6,10,0,ironBlock)
blockSetter.setBlock(-7,10,0,ironBlock)
blockSetter.setBlock(3,10,0,ironBlock)
blockSetter.setBlock(4,10,0,ironBlock)
blockSetter.setBlock(5,10,0,ironBlock)
blockSetter.setBlock(6,10,0,ironBlock)
blockSetter.setBlock(7,10,0,ironBlock)
blockSetter.setBlock(-3,11,0,ironBlock)
blockSetter.setBlock(-4,11,0,ironBlock)
blockSetter.setBlock(-5,11,0,ironBlock)
blockSetter.setBlock(-6,11,0,ironBlock)
blockSetter.setBlock(-7,11,0,ironBlock)
blockSetter.setBlock(3,11,0,ironBlock)
blockSetter.setBlock(4,11,0,ironBlock)
blockSetter.setBlock(5,11,0,ironBlock)
blockSetter.setBlock(6,11,0,ironBlock)
blockSetter.setBlock(7,11,0,ironBlock)
blockSetter.setBlock(-3,12,0,ironBlock)
blockSetter.setBlock(-4,12,0,ironBlock)
blockSetter.setBlock(-5,12- железо
blockSetter.setBlock(-6,12,0,ironBlock)
blockSetter.setBlock(-7,12,0,ironBlock)
blockSetter.setBlock(3,12,0,ironBlock)
blockSetter.setBlock(4,12,0,ironBlock)
blockSetter.setBlock(5,12,0,ironBlock)
blockSetter.setBlock(6,12,0,ironBlock)
blockSetter.setBlock(7,12,0,ironBlock)
blockSetter.setBlock(-3,13,0,ironBlock)
blockSetter.setBlock(-4,13,0,ironBlock)
blockSetter.setBlock(-5,13,0,ironBlock)
blockSetter.setBlock(-6,13,0,ironBlock)
blockSetter.setBlock(-7,13,0,ironBlock)
blockSetter.setBlock(3,13,0,ironBlock)
blockSetter.setBlock(4,13,0,ironBlock)
blockSetter.setBlock(5,13,0,ironBlock)
blockSetter.setBlock(6,13,0,ironBlock)
blockSetter.setBlock(7,13,0,ironBlock)
blockSetter.setBlock(-3,14,0,ironBlock)
blockSetter.setBlock(-4,14,0,ironBlock)
blockSetter.setBlock(-5,14,0,ironBlock)
blockSetter.setBlock(-6,14,0,ironBlock)
blockSetter.setBlock(-7,14,0,ironBlock)
blockSetter.setBlock(3,14,0,ironBlock)
blockSetter.setBlock(4,14,0,ironBlock)
blockSetter.setBlock(5,14,0,ironBlock)
blockSetter.setBlock(6,14,0,ironBlock)
blockSetter.setBlock(7,14,0,ironBlock)
blockSetter.setBlock(-3,15,0,ironBlock)
blockSetter.setBlock(-4,15,0,ironBlock)
blockSetter.setBlock(-5,15,0,ironBlock)
blockSetter.setBlock(-6,15,0,ironBlock)
blockSetter.setBlock(-7,15,0,ironBlock)
blockSetter.setBlock(3,15,0,ironBlock)
blockSetter.setBlock(4,15,0,ironBlock)
blockSetter.setBlock(5,15,0,ironBlock)
blockSetter.setBlock(6,15,0,ironBlock)
blockSetter.setBlock(7,15,0,ironBlock)
blockSetter.setBlock(-5,13,0,ironBlock)
blockSetter.setBlock(-5,14,0,ironBlock)
blockSetter.setBlock(-5,15,0,ironBlock)
blockSetter.setBlock(-5,16,0,ironBlock)
blockSetter.setBlock(-5,17,0,ironBlock)
blockSetter.setBlock(-5,18,0,ironBlock)
blockSetter.setBlock(-5,19,0,ironBlock)
blockSetter.setBlock(-5,20,0,ironBlock)
blockSetter.setBlock(-5,21,0,ironBlock)
blockSetter.setBlock(-5,22,0,ironBlock)
blockSetter.setBlock(-5,23,0,ironBlock)
blockSetter.setBlock(-5,24,0,ironBlock)
blockSetter.setBlock(-5,25,0,ironBlock)
blockSetter.setBlock(-4,13,0,ironBlock)
blockSetter.setBlock(-4,14,0,ironBlock)
blockSetter.setBlock(-4,15,0,ironBlock)
blockSetter.setBlock(-4,16,0,ironBlock)
blockSetter.setBlock(-4,17,0,ironBlock)
blockSetter.setBlock(-4,18,0,ironBlock)
blockSetter.setBlock(-4,19,0,ironBlock)
blockSetter.setBlock(-4,20,0,ironBlock)
blockSetter.setBlock(-4,21,0,ironBlock)
blockSetter.setBlock(-4,22,0,ironBlock)
blockSetter.setBlock(-4,23,0,ironBlock)
blockSetter.setBlock(-4,24,0,ironBlock)
blockSetter.setBlock(-4,25,0,ironBlock)
blockSetter.setBlock(-3,13,0,ironBlock)
blockSetter.setBlock(-3,14,0,ironBlock)
blockSetter.setBlock(-3,15,0,ironBlock)
blockSetter.setBlock(-3,16,0,ironBlock)
blockSetter.setBlock(-3,17,0,ironBlock)
blockSetter.setBlock(-3,18,0,ironBlock)
blockSetter.setBlock(-3,19,0,ironBlock)
blockSetter.setBlock(-3,20,0,ironBlock)
blockSetter.setBlock(-3,21,0,ironBlock)
blockSetter.setBlock(-3,22,0,ironBlock)
blockSetter.setBlock(-3,23,0,ironBlock)
blockSetter.setBlock(-3,24,0,ironBlock)
blockSetter.setBlock(-3,25,0,ironBlock)
blockSetter.setBlock(-2,13,0,ironBlock)
blockSetter.setBlock(-2,14,0,ironBlock)
blockSetter.setBlock(-2,15,0,ironBlock)
blockSetter.setBlock(-2,16,0,ironBlock)
blockSetter.setBlock(-2,17,0,ironBlock)
blockSetter.setBlock(-2,18,0,ironBlock)
blockSetter.setBlock(-2,19,0,ironBlock)
blockSetter.setBlock(-2,20,0,ironBlock)
blockSetter.setBlock(-2,21,0,ironBlock)
blockSetter.setBlock(-2,22,0,ironBlock)
blockSetter.setBlock(-2,23,0,ironBlock)
blockSetter.setBlock(-2,24,0,ironBlock)
blockSetter.setBlock(-2,25,0,ironBlock)
blockSetter.setBlock(-1,13,0,ironBlock)
blockSetter.setBlock(-1,14,0,ironBlock)
blockSetter.setBlock(-1,15,0,ironBlock)
blockSetter.setBlock(-1,16,0,ironBlock)
blockSetter.setBlock(-1,17,0,ironBlock)
blockSetter.setBlock(-1,18,0,ironBlock)
blockSetter.setBlock(-1,19,0,ironBlock)
blockSetter.setBlock(-1,20,0,ironBlock)
blockSetter.setBlock(-1,21,0,ironBlock)
blockSetter.setBlock(-1,22,0,ironBlock)
blockSetter.setBlock(-1,23,0,ironBlock)
blockSetter.setBlock(-1,24,0,ironBlock)
blockSetter.setBlock(-1,25,0,ironBlock)
blockSetter.setBlock(0,13,0,ironBlock)
blockSetter.setBlock(0,14,0,ironBlock)
blockSetter.setBlock(0,15,0,ironBlock)
blockSetter.setBlock(0,16,0,ironBlock)
blockSetter.setBlock(0,17,0,ironBlock)
blockSetter.setBlock(0,18,0,ironBlock)
blockSetter.setBlock(0,19,0,ironBlock)
blockSetter.setBlock(0,20,0,ironBlock)
blockSetter.setBlock(0,21,0,ironBlock)
blockSetter.setBlock(0,22,0,ironBlock)
blockSetter.setBlock(0,23,0,ironBlock)
blockSetter.setBlock(0,24,0,ironBlock)
blockSetter.setBlock(0,25,0,ironBlock)
blockSetter.setBlock(1,13,0,ironBlock)
blockSetter.setBlock(1,14,0,ironBlock)
blockSetter.setBlock(1,15,0,ironBlock)
blockSetter.setBlock(1,16,0,ironBlock)
blockSetter.setBlock(1,17,0,ironBlock)
blockSetter.setBlock(1,18,0,ironBlock)
blockSetter.setBlock(1,19,0,ironBlock)
blockSetter.setBlock(1,20,0,ironBlock)
blockSetter.setBlock(1,21,0,ironBlock)
blockSetter.setBlock(1,22,0,ironBlock)
blockSetter.setBlock(1,23,0,ironBlock)
blockSetter.setBlock(1,24,0,ironBlock)
blockSetter.setBlock(1,25,0,ironBlock)
blockSetter.setBlock(2,13,0,ironBlock)
blockSetter.setBlock(2,14,0,ironBlock)
blockSetter.setBlock(2,15,0,ironBlock)
blockSetter.setBlock(2,16,0,ironBlock)
blockSetter.setBlock(2,17,0,ironBlock)
blockSetter.setBlock(2,18,0,ironBlock)
blockSetter.setBlock(2,19,0,ironBlock)
blockSetter.setBlock(2,20,0,ironBlock)
blockSetter.setBlock(2,21,0,ironBlock)
blockSetter.setBlock(2,22,0,ironBlock)
blockSetter.setBlock(2,23,0,ironBlock)
blockSetter.setBlock(2,24,0,ironBlock)
blockSetter.setBlock(2,25,0,ironBlock)
blockSetter.setBlock(3,13,0,ironBlock)
blockSetter.setBlock(3,14,0,ironBlock)
blockSetter.setBlock(3,15,0,ironBlock)
blockSetter.setBlock(3,16,0,ironBlock)
blockSetter.setBlock(3,17,0,ironBlock)
blockSetter.setBlock(3,18,0,ironBlock)
blockSetter.setBlock(3,19,0,ironBlock)
blockSetter.setBlock(3,20,0,ironBlock)
blockSetter.setBlock(3,21,0,ironBlock)
blockSetter.setBlock(3,22,0,ironBlock)
blockSetter.setBlock(3,23,0,ironBlock)
blockSetter.setBlock(3,24,0,ironBlock)
blockSetter.setBlock(3,25,0,ironBlock)
blockSetter.setBlock(4,13,0,ironBlock)
blockSetter.setBlock(4,14,0,ironBlock)
blockSetter.setBlock(4,15,0,ironBlock)
blockSetter.setBlock(4,16,0,ironBlock)
blockSetter.setBlock(4,17,0,ironBlock)
blockSetter.setBlock(4,18,0,ironBlock)
blockSetter.setBlock(4,19,0,ironBlock)
blockSetter.setBlock(4,20,0,ironBlock)
blockSetter.setBlock(4,21,0,ironBlock)
blockSetter.setBlock(4,22,0,ironBlock)
blockSetter.setBlock(4,23,0,ironBlock)
blockSetter.setBlock(4,24,0,ironBlock)
blockSetter.setBlock(4,25,0,ironBlock)
blockSetter.setBlock(5,13,0,ironBlock)
blockSetter.setBlock(5,14,0,ironBlock)
blockSetter.setBlock(5,15,0,ironBlock)
blockSetter.setBlock(5,16,0,ironBlock)
blockSetter.setBlock(5,17,0,ironBlock)
blockSetter.setBlock(5,18,0,ironBlock)
blockSetter.setBlock(5,19,0,ironBlock)
blockSetter.setBlock(5,20,0,ironBlock)
blockSetter.setBlock(5,21,0,ironBlock)
blockSetter.setBlock(5,22,0,ironBlock)
blockSetter.setBlock(5,23,0,ironBlock)
blockSetter.setBlock(5,24,0,ironBlock)
blockSetter.setBlock(5,25,0,ironBlock)
blockSetter.setBlock(-4,26,0,ironBlock)
blockSetter.setBlock(-3,26,0,ironBlock)
blockSetter.setBlock(-2,26,0,ironBlock)
blockSetter.setBlock(-1,26,0,ironBlock)
blockSetter.setBlock(0,26,0,ironBlock)
blockSetter.setBlock(1,26,0,ironBlock)
blockSetter.setBlock(2,26,0,ironBlock)
blockSetter.setBlock(3,26,0,ironBlock)
blockSetter.setBlock(4,26,0,ironBlock)
blockSetter.setBlock(-3,27,0,ironBlock)
blockSetter.setBlock(-2,27,0,ironBlock)
blockSetter.setBlock(-1,27,0,ironBlock)
blockSetter.setBlock(0,27,0,ironBlock)
blockSetter.setBlock(1,27,0,ironBlock)
blockSetter.setBlock(2,27,0,ironBlock)
blockSetter.setBlock(3,27,0,ironBlock)
blockSetter.setBlock(-2,28,0,ironBlock)
blockSetter.setBlock(-2,29,0,ironBlock)
blockSetter.setBlock(-1,28,0,ironBlock)
blockSetter.setBlock(-1,29,0,ironBlock)
blockSetter.setBlock(0,28,0,ironBlock)
blockSetter.setBlock(0,29,0,ironBlock)
blockSetter.setBlock(1,28,0,ironBlock)
blockSetter.setBlock(1,29,0,ironBlock)
blockSetter.setBlock(2,28,0,ironBlock)
blockSetter.setBlock(2,29,0,ironBlock)
blockSetter.setBlock(-1,30,0,ironBlock)
blockSetter.setBlock(-1,31,0,ironBlock)
blockSetter.setBlock(-1,32,0,ironBlock)
blockSetter.setBlock(-1,33,0,ironBlock)
blockSetter.setBlock(-1,34,0,ironBlock)
blockSetter.setBlock(0,30,0,ironBlock)
blockSetter.setBlock(0,31,0,ironBlock)
blockSetter.setBlock(0,32,0,ironBlock)
blockSetter.setBlock(0,33,0,ironBlock)
blockSetter.setBlock(0,34,0,ironBlock)
blockSetter.setBlock(1,30,0,ironBlock)
blockSetter.setBlock(1,31,0,ironBlock)
blockSetter.setBlock(1,32,0,ironBlock)
blockSetter.setBlock(1,33,0,ironBlock)
blockSetter.setBlock(1,34,0,ironBlock)
blockSetter.setBlock(0,35,0,ironBlock)
blockSetter.setBlock(0,36,0,ironBlock)

for i in range(100):
   time.sleep(1)
   rocketShape.moveBy(0,1,0)

rocketShape.clear()
