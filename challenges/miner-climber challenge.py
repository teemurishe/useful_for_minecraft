import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print("Добро пожаловать в шахтёр-горник челлендж! Ваша цель - Спуститься как можно ниже и забраться как можно выше в течение ровно 1 минуты! До начала челленджа осталось 5 секунд!")
time.sleep(10)
mc.postToChat("Челлендж начинается!")

heights = [300, -100]
count = 0

while count < 60:
    pos = mc.player.getTilePos()
    if pos.y < heights[0]:
        heights[0] = pos.y
    elif pos.y > heights[1]:
        heights[1] = pos.y
    
    count += 1
    time.sleep(1)

mc.postToChat("Челлендж завершён! Пришло время результатов!")

mc.postToChat("Низшая позиция: ",+str(heights[0]))
mc.postToChat("Высшая позиция: ",+str(heights[1]))
time.sleep(3)

if heights[0] < -50:
    mc.postToChat("Да вы прирождённый шахтёр! Ну шахтёр получает по заслугам за свой нелёгкий труд!")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 56)
elif heights[0] < -100:
    mc.postToChat("Либо ты читер, либо ты реально шахтёр... Наверное, не надо читеров награждать :)")
    
if heights[1] > 50:
    mc.postToChat("Вы настоящий майнкрафтовский альпинист! Ну а за такое и награды не жалко!")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 80)
    mc.setBlock(pos.x, pos.y + 1, pos.z, 80)
elif heights[1] > 100:
    mc.postToChat("СЛЫШ, А НУ ФЛАЙ ОТРУБИ! награду он тут ещё ждёт...")
print("Челлендж завершён, программа остановлена. Благодарим за использование и ждём Вас снова!")
