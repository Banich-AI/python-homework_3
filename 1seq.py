question_num = int(input('Введите количество элементов: '))

numb = []
for num in range(question_num):
    answer = int(input(f'Введите {num + 1} число: '))
    numb.append(answer)
numb.sort()
print(numb)
