numbers = input('Введите произвольное количество чисел, через запятую ')
print(set(numbers.replace('/',',').split(',')))

