immutable_var = 1,'banana',2,"books",3,'pens'
print(immutable_var)
#immutable_var [0] = 4
#print(immutable_var)
# Кортеж - неизменяемы обьект. Кортежи хранят данные, к которым можно обратиться, но нельзя изменить. Однако кортежи занимают меньше места чем списки.
# Строки 3 и 4, в которых, согласно заданию, пытался изменить кортеж закоментировал
mutable_list = [1,'banana',2,"books",3,'pens']
print(mutable_list)
mutable_list[0] = 22
mutable_list[1] = 'apples'
mutable_list[2]=31
mutable_list[3]='copybooks'
mutable_list[4]=17
mutable_list[5]='pencils'
print(mutable_list)