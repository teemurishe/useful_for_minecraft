from mcpi.minecraft import Minecraft
mc = Minecraft.create()

file = open('new_file.txt', 'w', encoding = 'utf-8')
answer = ''
while True:
    answer = input('Введите ваше дело: ')
    if answer == 'выход':
        break
    file.write(answer)
    file.write(' \n')
 
file.close()
