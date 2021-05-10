from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

print(
    'Proudly presenting an utilities kit for Minecraft! Please, choose the instrument you need:')

print('1. Block setting using Python-coordinates')
print('2. Flat surface building')
print('3. Teleport to death place')
print('4. Random teleportation')
print('5. Teleportation using Python coordinates')
print('6. EXPLODE EVERYTHING!!!')


def beginProgramm():
    pass


def blockSetter():
    x = int(input("X coordinate: "))
    y = int(input("Y coordinate: "))
    z = int(input("Z coordinate: "))
    id = int(input("Block ID: "))
    mc.setBlock(x, y, z, id)


def flatPattern():
    pos = mc.player.getTilePos()
    x, y, z = pos.x, pos.y, pos.z
    air, grass = 0, 2

    aw = int(input("Flat area's side length: "))
    ah, al = 256, aw
    gw.gh, gl = al, 1, gw

    mc.setBlocks(x, y, z, x + aw, y + ah, z + al, air)
    mc.setBlocks(x, y, z, x + gw, y + gh, z + gl, grass)


def deathSaver():
    pos = mc.player.getTilePos()
    print('Teleportation coordinates: ' + str(pos))
    time.sleep(2)
    mc.player.setTilePos(pos)


def randTeport():
    pos = mc.player.getTilePos()
    mc.postToChat('Your current position: ' + str(pos))

    x = random.randint(1, 10000)
    y = random.randint(50, 80)
    z = random.randint(1, 10000)
    mc.player.setPos(x, y, z)

    posn = mc.player.getTilePos()
    xb, yb, zb = posn.x, posn.y, posn.z
    grass = 2
    width, height, length = 3, 1, 3
    mc.setBlocks(xb, yb, zb, xb + width - 1, yb + height - 1, zb + length - 1, grass)

    xn, yn, zn = xb + 2, yb + 1, zb + 2
    mc.player.setPos(xn, yn, zn)

    posf = mc.player.getTilePos()
    mc.postToChat('Your new position in Python coordinates: ' + str(posf))


def pyTeleport():
    x = int(input("X coordinate: "))
    y = int(input("Y coordinate: "))
    z = int(input("Z coordinate: "))
    mc.player.setTilePos(x, y, z)


def tntSetter():
    mc.postToChat("Please, get placed to the explosion place. 5 seconds to getting your current position...")
    time.sleep(5)
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    tnt = 46
    fire = 51
    mc.postToChat("WARNING!!! To avoid bugs, get away on 20-50 blocks and enjoy the sught! Your coordinates are got succesful :)")
    print("WARNING!!! To avoid bugs, get away on 20-50 blocks and enjoy the sught! Your coordinates are got succesful :)")
    w = int(input('TNT cube\'s side length: '))
    h = w
    l = h
    mc.setBlocks(x, y, z, x + w, y + h, z + l, tnt)
    mc.setBlock(x + 1, y + 1, z + 1, fire)


while choice != 'Stop':
    choice = input('Choose utilite: ')
    print('To finish work with kit, enter "Stop"')

    if choice == '1':
        blockSetter()
    if choice == '2':
        flatPattern()
    if choice == '3':
        deathSaver()
    if choice == '4':
        randTeport()
    if choice == '5':
        pyTeleport()
    if choice == '6':
        tntSetter()
