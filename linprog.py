import numpy as np
from math import inf

def count_columns(A):
    return len(A[0, :])


def count_rows(A):
    return len(A[:, 0])


# Cоздает матрицу
# cons + 1 строк для ограничений и строки функции
# cons + var + 2 столбцов для переменных - изначальные и добавочные переменные, столбец b 
def create_matrix(var, cons):
    tab = np.zeros((cons+1, var+cons+2))
    return tab


# Есть ли отрицательный элемент в последнем столбце (b)
def is_negative_b(table):
    minim = min(table[:-1, -1])
    if minim >= 0:
        return False
    else:
        return True


# Есть ли отрицательный элемент в последней строке (строке функции)
def is_negative_c(table):
    minim = min(table[count_rows(table)-1, :-1])
    if minim >= 0:
        return False
    else:
        return True


# Поиск минимального элемента в последнем столбце (b)
def find_negative_b(table):
    lc = count_columns(table)
    minim = min(table[:-1, lc-1])
    if minim <= 0:
        n = np.where(table[:-1, lc-1] == minim)[0][0]
    else:
        n = None
    return n


# Поиск минимального элемента в последней строке (строке функции)
def find_negative_c(table):
    lr = count_rows(table)
    minim = min(table[lr-1, :-1])
    if minim <= 0:
        n = np.where(table[lr-1, :-1] == minim)[0][0]
    else:
        n = None
    return n


# Поиск разрешающего элемента для изменения столбца b
def find_razr_b(table):
    total = []
    razr_row_index = find_negative_b(table)
    razr_row = table[razr_row_index, :-1]
    minim = min(razr_row)
    razr_col_index = np.where(razr_row == minim)[0][0]
    razr_col = table[:-1, razr_col_index]
    for a, b in zip(razr_col, table[:-1, -1]):
        if a**2 > 0 and b/a > 0:
            total.append(b/a)
        else:
            total.append(inf)
    index = total.index(min(total))
    return [index, razr_col_index]


# Поиск разрешающего элемента
def find_razr_c(table):
    if is_negative_c(table):
        total = []
        negative = find_negative_c(table)
        for a, b in zip(table[:-1, negative], table[:-1, -1]):
            if b/a > 0 and a**2 > 0:
                total.append(b/a)
            else:
                total.append(inf)
        index = total.index(min(total))
        return [index, negative]


# Модифицированный шаг жорданова исключения
def jordan(row, col, table):
    lr = count_rows(table)
    lc = count_columns(table)
    new_table = np.zeros((lr, lc))
    razr_row = table[row, :]
    if table[row, col]**2 > 0:
        delimeter = 1/table[row, col]
        r = razr_row*delimeter
        for i in range(count_rows(table)):
            i_row = table[i, :]
            b = table[i, col]
            if list(i_row) == list(razr_row):
                continue
            else:
                new_table[i, :] = list(i_row-r*b)
        new_table[row, :] = list(r)
        return new_table
    else:
        print('Something went wrong on jordan step')


# Преобразует таблицу для минимизации
def convert_min(table):
    table[-1, :-2] = [-1*i for i in table[-1, :-2]]
    table[-1, -1] = -1*table[-1, -1]
    return table


# Создает список строк со значениями ['x1','x2',...]
def list_of_x(table):
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

# Заполняет таблицу из матриц
def fill_table(A, b, c, table):
    for row, i in [(A[i, :], i) for i in range(count_rows(A))]:
        table_row = table[i, :]
        j = 0
        while j < len(row):
            table_row[j] = row[j]
            j += 1
        table_row[-1] = b[i]
        table_row[count_columns(table) - count_rows(table) - 1 + i] = 1
    row = table[count_rows(table) - 1, :]
    i = 0
    while i < len(c)-1:
        row[i] = c[i]*-1
        i += 1
    row[-2] = 1
    row[-1] = c[-1]


# Решение таблицы
def solve_table(table, minim=True):
    if minim:
        table = convert_min(table)
    while is_negative_b(table) == True:
        table = jordan(find_razr_b(table)[0], find_razr_b(table)[1], table)
    while is_negative_c(table) == True:
        table = jordan(find_razr_c(table)[0], find_razr_c(table)[1], table)
    lc = count_columns(table)
    lr = count_rows(table)
    var = lc - lr - 1
    i = 0
    val = {}
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[list_of_x(table)[i]] = table[loc, -1]
        else:
            val[list_of_x(table)[i]] = 0
    if minim:
        val['min'] = table[-1, -1]*-1
    else:
        val['max'] = table[-1, -1]
    return val


def simplex(A, b, c, minim=True):
    table = create_matrix(count_columns(A), count_rows(A))
    fill_table(A, b, c, table)
    print(table)
    return solve_table(table, minim)


A = np.array([[2, 3, 1, 2], [2, -1, 2, 1], [1, 1, 0, -1]])
b = [3, 4, 1]
c = [-2, 1, -1, 3]


if __name__ == "__main__":
    print(simplex(A, b, c))
