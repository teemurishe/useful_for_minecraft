from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
pos = mc.player.getTilePos()
print(pos)
time.sleep(10)
mc.player.setTilePos(pos)