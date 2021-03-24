from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

print(pos)

mc.postToChat("Я Арбузус, бог арбузов! Я явился, чтобы забрать дань! Где твой алтарь, слуга мой? Заговори же со мною на языке божественном, что Python зовётся! Открой же портал ты, что средою зовёшь ты!")
ax = int(input("Каково же его положение по первой горизонтали земной? "))
ay = int(input("И каково же его положение в выси небесной? "))
az = int(input("Ну и как же лежит он в длине неземной? "))
gift = mc.getBlock(ax, ay + 1, az)
print("Вижу алтарь я твой, ставь же дар свой на него! 10 тебе секунд на то, чтобы подношение принести! Время пошло...")
time.sleep(10)
if gift != 0:
    mc.postToChat("Вижу дар я твой, дай же время, дабы смог я тебя наградить, иль же покарать за неверность!")
    time.sleep(5)
    if gift == 57:
        mc.postToChat("Алмаз - не арбуз, но спасибо!")
        mc.setBlock(ax, ay + 1, az, 0)
    if gift == 103:
        mc.postToChat("Я принимаю твоё подношение и поощряю твою верность!")
        mc.setBlock(ax, ay + 1, az, 56)
    elif gift == 6:
        mc.postToChat("Да как ты смеешь подавать мне жалкий кустик?! ГОРИ В АДУ, ОТСТУПНИК!!!")
        pos = mc.player.getTilePos()
        x = pos.x
        y = pos.y
        z = pos.z
        mc.setBlock(x, y, z, 90)
    else:
        mc.postToChat("Это не арбуз! За столь дерзкий поступок ты будешь сослан навеки!")
if gift == 0:
    mc.postToChat("Ничего не поднёс ты мне, да как ты посмел?! Так спрячься же ты в глуби земной, да не являйся вновь на свет сий!")
    mc.player.setTilePos(0, -100, 0)
