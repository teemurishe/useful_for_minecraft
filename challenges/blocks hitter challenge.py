import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(60)

hits = mc.events.pollBlockHits()
block = 103
mc.postToChat("Welcome to new mini-game! Hit as many blocks as you can! 5! 4! 3...")
time.sleep(5)
for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.player.setPos(x,y,z)
    time.sleep(10)
mc.postToChat("So, you have hit" + str(len(hits)) + "blocks!")
if len(hits) < 30:
    mc.postToChat("Not bad! This is your prize :)")
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 42)
if len(hits) < 10:
    mc.postToChat("Ahahah, lol! Goodbye!")
    mc.setBlock(pos.x, pos.y, pos.z, 90)
if len(hits) < 50:
    mc.postToChat("Wow, hello, cookie-clicker player! Have your diamonds!")
    mc.setBlock(pos.x, pos.y, pos.z, 57)
    mc.setBlock(pos.x, pos.y + 1, pos.z, 57)
if len(hits) < 80:
    mc.postToChat("Turn off your macrosses and go to The End!")
    mc.setBlock(pos.x, pos.y, pos.z, 119)
print("Program stopped. Hope to see you again!")
