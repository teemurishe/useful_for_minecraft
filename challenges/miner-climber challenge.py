import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print("Welcome to the miner-climber challenge! Your goal: Climb down and up as low and as high as it's possible during a minute!\
5 seconds to beginning!")
time.sleep(10)
mc.postToChat("Let's go!")

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

mc.postToChat("Challenge finished! Time to discover your results!")

mc.postToChat("Низшая позиция: ",+str(heights[0]))
mc.postToChat("Высшая позиция: ",+str(heights[1]))
time.sleep(3)

if heights[0] < -50:
    mc.postToChat("Wow, you're inborn miner! As you know, good miners get a lot of money...")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 56)
elif heights[0] < -100:
    mc.postToChat("It seems you're CHEATER!... And cheaters don't get prizes :)")
    
if heights[1] > 50:
    mc.postToChat("You're real climber! Get your climber reward!")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 80)
    mc.setBlock(pos.x, pos.y + 1, pos.z, 80)
elif heights[1] > 100:
    mc.postToChat("TURN OFF YOUR FLY CHEATS! Do you want any reward after that?..")
print("Challenge finished, program stopped. Thanks for using and see you again!")
