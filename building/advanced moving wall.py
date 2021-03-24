from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import minecraftstuff
import threading

brick = 45


def moveWall():
    pos = mc.player.getTilePos()
    wallPos = pos.clone()

    wallShape = minecraftstuff.MinecraftShape(mc, wallPos)
    wallShape.setBlocks(0, 0, 0, 0, 0, 9, brick)

    while True:
        wallShape.moveBy(0, 1, 0)
        time.sleep(1)
        wallShape.moveBy(0, -1, 0)
        time.sleep(1)


def river():
    pos = mc.player.getTilePos()

    bridgePos = pos.clone()

    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos)

    bridgeShape.setBlocks(0, 0, 0, 3, 0, 3, 5)

    while True:
        for left in range(0, 10):
            bridgeShape.moveBy(1, 0, 0)
            time.sleep(1)
        for right in range(0, 10):
            bridgeShape.moveBy(-1, 0, 0)
            time.sleep(1)


wall_t = threading.Thread(target=moveWall)
wall_t.start()

river_t = threading.Thread(target=river)
river_t.start()

mc.postToChat('This program started!')
