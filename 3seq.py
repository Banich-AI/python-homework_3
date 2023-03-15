first_list = input('Введите значения первого спистка ')
second_list = input(('Введите значения второго списка '))

result_list = (set(first_list) - set(second_list))
print(list(result_list),'есть тольк в первом списке')