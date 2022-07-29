# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


init_string = 'абвгдейка - это передача'

def filter_text(some_text):
    some_text = some_text.split(' ')
    func = lambda word: 'абв' not in word
    return ' '.join(list(filter(func, some_text)))

print(filter_text(init_string))

