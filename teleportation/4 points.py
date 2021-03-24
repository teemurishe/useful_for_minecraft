from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

mc.postToChat("10 seconds to teleportation to point 1")
time.sleep(5)
mc.postToChat("5 seconds to teleportation to point 1")
time.sleep(5)
x1 = 0
y1 = 70
z1 = 0
mc.player.setTilePos(x1, y1, z1)
mc.postToChat("Teleportation to point 1 succesful!")

mc.postToChat("10 seconds to teleportation to point 2")
time.sleep(5)
mc.postToChat("5 seconds to teleportation to point 2")
time.sleep(5)
x2 = -50
y2 = -60
z2 = -1300
mc.player.setTilePos(x2, y2, z2)
mc.postToChat("Teleportation to point 2 succesful!")

mc.postToChat("10 seconds to teleportation to point 3")
time.sleep(5)
mc.postToChat("5 seconds to teleportation to point 3")
time.sleep(5)
x3 = -508.56
y3 = 60.92
z3 = 1300.7
mc.player.setPos(x3, y3, z3)
mc.postToChat("Teleportation to point 3 succesful!")

mc.postToChat("10 seconds to teleportation to point 4")
time.sleep(5)
mc.postToChat("5 seconds to teleportation to point 4")
time.sleep(5)
x4 = 367.9
y4 = 10.6
z4 = -547.3
mc.player.setPos(x4, y4, z4)
mc.postToChat("Teleportation to point 4 succesful!")

mc.postToChat("Series of teleportations finished succesful")
