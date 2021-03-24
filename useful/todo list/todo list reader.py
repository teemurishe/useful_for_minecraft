from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
 
file = open('new_file.txt', 'r', encoding = 'utf-8')
for line in file:
    mc.postToChat(line)
    time.sleep(3)
