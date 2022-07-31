# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах


with open('sample_init.txt', 'r') as file:
    text = file.read()

def RLE_encode(init_text):
    encoding = ''
    prev_char = ''
    count = 1
    for i in init_text:
        if i !=prev_char:
            if prev_char:
                encoding = encoding + str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count = count + 1
    return encoding
encoded = RLE_encode(text)
print(encoded)

with open('sample_encoded.txt', 'r') as file:
    text2 = file.read()

def RLE_decode(init_text):
    count = ''
    str_decode = ''
    for char in init_text:
        if char.isdigit():
            count = count + char
        else:
            str_decode = str_decode + char * int(count)
            count = ''
    return str_decode

decoded = RLE_decode(text2)
print(decoded)