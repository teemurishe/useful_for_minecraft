from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()                    #Получаем позицию игрока

x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock (x-1, y-1, z-1)

mc.postToChat("Игрок летает или прыгает: " + str(blockType == 0))