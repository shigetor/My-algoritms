import time

"""Бинарный поиск"""


def binary_research(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess >= item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def linres2(list, item):
    i = 1
    list_lenght = len(list)
    index = 0
    while index <= (list_lenght - 1):
        if list[index] == item:
            if index < list_lenght:
                return f'Искомое значение найдено, его индекс {index}'
            elif index >= list_lenght:
                break
        index += 1


def linear_research_3(list, item):
    i = 1
    list_lenght = len(list)
    index = 0

    while index <= (list_lenght - 1):
        if list[index] == item:
            if index < list_lenght:
                return f'Искомое значение найдено, его индекс {index}'
            elif index >= list_lenght:
                break
        elif list[index ] != item:
            index += 2
        else:
            index += 1
