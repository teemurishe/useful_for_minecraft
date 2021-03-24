from mcpi.minecraft import Minecraft
mc = Minecraft.create()

file = open('new_file.txt', 'w', encoding = 'utf-8')
answer = ''
print('Print "Exit" to finish the work of program')
while True:
    answer = input('Enter your business: ')
    if answer == 'Exit':
        break
    file.write(answer)
    file.write(' \n')

file.close()
