from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

print(pos)

mc.postToChat("I'm Watermelonner, the watermelons' God! I'm going to take your\
money! Where is your altar, slave? Open the portal, that you call the console!")
ax = int(input("What is its position along the first earthly horizontal? "))
ay = int(input("And what is his position in the heights of heaven? "))
az = int(input("Well, how does it lie in unearthly length? "))
gift = mc.getBlock(ax, ay + 1, az)
print("I see your table, put your gift on it! 10 seconds for you to bring an\
offering! Time is going ...")
time.sleep(10)
if gift != 0:
    mc.postToChat("I see your gift, give me some time...")
    time.sleep(5)
    if gift == 57:
        mc.postToChat("Diamond is not watermelon, but thanks!")
        mc.setBlock(ax, ay + 1, az, 0)
    if gift == 103:
        mc.postToChat("Wow, you are so faithful!")
        mc.setBlock(ax, ay + 1, az, 56)
    elif gift == 6:
        mc.postToChat("I'll burn you in Nether, apostate!")
        pos = mc.player.getTilePos()
        x = pos.x
        y = pos.y
        z = pos.z
        mc.setBlock(x, y, z, 90)
    else:
        mc.postToChat("It's not a watermelon...")
if gift == 0:
    mc.postToChat("Where is the gift?! Goodbye...")
    mc.player.setTilePos(0, -100, 0)
