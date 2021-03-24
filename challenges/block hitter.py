from mcpi.minecraft import minecraft
mc = minecraft.create()
import time

time.sleep(60)

blockHits = mc.events.pollBlockHits
count = len(blockHits)

mc.postToChat("Your score: " + str(count))
