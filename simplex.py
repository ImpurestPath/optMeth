import numpy as np


def func(c, x):
    sum = 0
    for index, c_element in enumerate(c):
        sum += c_element*x[index]
    return sum


def jordan(A, razr_row, razr_column):
    # Сохраняем старые данные
    A_old = A.copy()
    razr_element = A.item(razr_row, razr_column)

    # Изменяем разрешаюший элемент
    A.itemset((razr_row, razr_column), 1.0 / razr_element)

    # Изменяем разрешающий столбец
    for index, element in np.ndenumerate(A_old[:, razr_column]):
        index = index[0]
        if index == razr_row:
            continue
        A.itemset((index, razr_column), -
                  A_old.item(index, razr_column) / razr_element)

    # Изменяем разрешающий столбец
    for index, element in np.ndenumerate(A_old[razr_row, :]):
        index = index[1]
        if index == razr_column:
            continue
        A.itemset((razr_row, index), A_old.item(razr_row, index)/razr_element)

    # Изменяем остальные элементы
    for index, element in np.ndenumerate(A_old):
        if (index[0] == razr_row or index[1] == razr_column):
            continue
        new_element = A_old.item(index) - 1. * A_old.item(razr_row, index[1]) * \
            A_old.item(index[0], razr_column) / razr_element
        A.itemset(index, new_element)
    return A


def check_negative(array):
    return not find_negative(array) is None


def find_negative(array):
    for index, element in enumerate(array):
        if (element < 0):
            return index
    return


def find_razr_row(array, b):
    min_number = -1
    razr_row = -1
    for index, element in enumerate(array):
        if element != 0 and index != array.size - 1:
            number = b[index]/element
            if (number > 0 and (number < min_number or min_number == -1)):
                min_number = number
                razr_row = index
    if min_number == -1:
        return
    return razr_row


def find_basic_plan(A):
    b = A[:, A.shape[1]-1].copy()

    # Если нет отрицательных, то возвращаем свободные члены
    if not check_negative(b):
        b.resize([A.shape[0]-1, 1], refcheck=False)
        return b

    # Избавляемся от отрицательных элементов и рекурсивно ищем опорный план
    negative_row = find_negative(b)
    razr_col = find_negative(A[negative_row, :A.shape[1] - 1].A1)
    if razr_col is None:
        return
    razr_row = find_razr_row(A[:, razr_col].A1, b)
    if razr_row is None:
        return
    print(A)
    return find_basic_plan(jordan(A, razr_row, razr_col))


def simplex(A, b, c, min=True):

    # Составляем симплексную таблицу
    table = A.copy()
    table = np.concatenate((table, b), axis=1)
    function_row = c.copy()
    function_row.resize([1, table.shape[1]], refcheck=False)
    function_row = function_row * -1
    table = np.concatenate((table, function_row), axis=0)
    
    # Ищем базовый план
    basic_plan = find_basic_plan(table)
    if basic_plan is None:
        print('No basic plan')
        return

    # Пока есть отрицательные числа в строке функции ищем оптимальный план
    while check_negative(table[table.shape[0]-1, :].A1):
        razr_column = -1

        # Ищем разрешающий столбец
        # TODO use function
        for index, element in np.ndenumerate(table[table.shape[0]-1, :]):
            index = index[1]
            if element < 0:
                razr_column = index
                break
        if razr_column == -1:
            return table[table.shape[0]-1, :].A1

        # Ищем разрешающую строку
        number = -1
        min_number = number
        razr_row = -1
        # TODO use function
        for index, element in np.ndenumerate(table[:, razr_column]):
            index = index[0]
            if element > 0 and index != table.shape[0] - 1:
                number = table.item(index, table.shape[1] - 1)/element
                if (number < min_number or min_number == -1):
                    min_number = number
                    razr_row = index
        if razr_row == -1:
            print('Infinite function')
            return
        
        # Делаем шаг модифицированного жорданова исключения
        table = jordan(table, razr_row, razr_column)

    # Опорный план найден, возвращаем коэффициенты функции 
    # TODO Нужно дополнить план нулями, если количество условий меньше количества переменных
    plan = np.flip(table[:, table.shape[1]-1].A1)
    
    return zeros