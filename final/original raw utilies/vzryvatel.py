from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
mc.postToChat("Встаньте на точку, где желаете соверщить взрыв. Ваши координаты будут записаны через 5 секунд.")
print("Встаньте на точку, где желаете соверщить взрыв. Ваши координаты будут записаны через 5 секунд.")
time.sleep(5)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
tnt = 46
fire = 51
mc.postToChat("ВНИМАНИЕ!!! Чтобы избежать зависаний в игре, отлетите на примерно 20-50 блоков и наслаждайтесь зрелищем! Ваши координаты уже записаны, поэтому взрывной кубик появится там, где Вы стояли ранее :)")
print("ВНИМАНИЕ!!! Чтобы избежать зависаний в игре, отлетите на примерно 20-50 блоков и наслаждайтесь зрелищем! Ваши координаты уже записаны, поэтому взрывной кубик появится там, где Вы стояли ранее :)")
w = int(input('Сторона взрывного кубика: '))
h = w
l = h
mc.setBlocks(x, y, z, x+w, y+h, z+l, tnt)
mc.setBlock(x+1, y+1, z+1, fire)