# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в 
# третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from functools import reduce

def create_list():
    with open('languages.txt', encoding='utf-8') as file:
        languages = file.read().split('\n')
    numbers = list(range(1,len(languages)+1))
    tuples_list = zip(numbers, [word.upper() for word in languages]) # привела к верхнему регистру каждое слово из списка languages и сделала кортежи
    return list(tuples_list)
my_list = create_list()


def filter_by_points (some_list):
    result_list = []
    result = 0
    for number, language in some_list:
        points = reduce(lambda a, b: a+b, [ord(char) for char in language])
        if points % number == 0:
            result = result + points
            result_list.append((points, language))
    del some_list
    return result, result_list

print(filter_by_points(my_list))