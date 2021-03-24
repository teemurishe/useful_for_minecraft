from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

mc.postToChat("10 секунд до телепортации в точку 1")
time.sleep(5)
mc.postToChat("5 секунд до телепортации в точку 1")
time.sleep(5)
x1 = 0
y1 = 70
z1 = 0
mc.player.setTilePos(x1, y1, z1)
mc.postToChat("Выполнена телепортация в точку 1")

mc.postToChat("10 секунд до телепортации в точку 2")
time.sleep(5)
mc.postToChat("5 секунд до телепортации в точку 2")
time.sleep(5)
x2 = -50
y2 = -60
z2 = -1300
mc.player.setTilePos(x2, y2, z2)
mc.postToChat("Выполнена телепортация в точку 2")

mc.postToChat("10 секунд до телепортации в точку 3")
time.sleep(5)
mc.postToChat("5 секунд до телепортации в точку 3")
time.sleep(5)
x3 = -508.56
y3 = 60.92
z3 = 1300.7
mc.player.setPos(x3, y3, z3)
mc.postToChat("Выполнена телепортация в точку 3")

mc.postToChat("10 секунд до телепортации в точку 4")
time.sleep(5)
mc.postToChat("5 секунд до телепортации в точку 4")
time.sleep(5)
x4 = 367.9
y4 = 10.6
z4 = -547.3
mc.player.setPos(x4, y4, z4)
mc.postToChat("Выполнена телепортация в точку 4")

mc.postToChat("Серия телепортаций окончена")