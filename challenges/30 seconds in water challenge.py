import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('Welcome to "30 seconds under water challenge"!')
mc.postToChat('When ready, enter "Start"')
starter = input("Waiting for the start challenge... ")
score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    mc.postToChat("Your score: " + str(score))
mc.postToChat("Final score: " + str(score))
if score > 15:
    mc.postToChat("Congratulations! You have been under water for already 15 seconds!")
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
if score > 20:
    pos = mc.player.getTilePos
    mc.setBlock(pos.x, pos.y, pos.z, 41)
    mc.postToChat("Wow! 20 seconds under water!")
if score > 30:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 264)
    mc.postToChat("Hoorah! Challeenge completed! Have some DIAMONDS!")
