
def is_int(input_number: str):
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        return False

def give_number (text: str, positive = True):
    num = ''
    while not num:
        num = is_int(input(text))
    if positive and num <= 0:
        return give_number(text, positive)
    return num 

def candy_can_take (text_message: str, max_count: int):
    it_can_be = True
    while it_can_be:
        max_for_step = give_number(text_message)
        if max_for_step > max_count:
            print(f'столько конфет взять нельзя, их всего {max_count}')
            continue
        it_can_be = False
    return max_for_step