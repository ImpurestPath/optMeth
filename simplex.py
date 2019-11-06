import numpy as np

#A = [[2,1,3,4],[1,-1,2,1],[0,0,1,3]]
#b = [[2],[4],[1]]
#c = [-2, 3, 4, -1]
def func(c,x):
    sum = 0
    for index, c_element in enumerate(c):
        sum += c_element*x[index]
    return sum


def jordan(A, razr_row, razr_column):
    A_old = A.copy()
    razr_element = A.item(razr_row, razr_column)
    A.itemset((razr_row, razr_column), 1.0 / razr_element)
    for index, element in np.ndenumerate(A_old[:, razr_column]):
        index = index[0]
        if index == razr_row:
            continue
        A.itemset((index, razr_column), -
                    A_old.item(index, razr_column) / razr_element)
    for index, element in np.ndenumerate(A_old[razr_row, :]):
        index = index[1]
        if index == razr_column:
            continue
        A.itemset((razr_row, index), A_old.item(razr_row, index)/razr_element)
    for index, element in np.ndenumerate(A_old):
        if (index[0] == razr_row or index[1] == razr_column):
            continue
        new_element = A_old.item(index) - 1. * A_old.item(razr_row, index[1]) * \
            A_old.item(index[0], razr_column) / razr_element
        A.itemset(index, new_element)
    return A

# def simplex(A, b, c, min=True):
#     A_new = A.copy();
#     #A_new = np.matrix('2 1 3 4; 1 -1 2 1; 0 0 1 3')
#     A_new = A.copy();
#     A_new = np.concatenate((A_new,b),axis=1)
#     function_row = c.copy()
#     function_row.resize([1, A_new.shape[1]], refcheck=False)
#     A_new = np.concatenate((A_new,function_row),axis=0)
    
#     while True:
#         razr_column = -1
#         for index, element in np.ndenumerate(A_new[A_new.shape[0]-1,:]):
#             index = index[1]
#             if element > 0:
#                 razr_column = index
#                 break
#         if razr_column == -1:
#             return A_new[A_new.shape[0]-1,:]
#         number = -1
#         min_number = number
#         razr_row = -1
#         for index, element in np.ndenumerate(A_new[:, razr_column]):
#             index = index[0]
#             if element > 0 and index != A_new.shape[0] - 1:
#                 number = A_new.item(index, A_new.shape[1] - 1)/element
#                 if (number < min_number or min_number == -1):
#                     min_number = number
#                     razr_row = index
#         if razr_row == -1:
#             print('Infinite function')
#             return
#         A_new = jordan(A_new,razr_row,razr_column)


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
    b = A[:,A.shape[1]-1].copy()
    if not check_negative(b):
        b.resize([A.shape[0]-1,1], refcheck=False)
        return b
    negative_row = find_negative(b)
    razr_col = find_negative(A[negative_row,:A.shape[1] -1].A1)
    if razr_col is None:
        return
    razr_row = find_razr_row(A[:,razr_col].A1,b)
    if razr_row is None:
        return
    print(A)
    return find_basic_plan(jordan(A,razr_row,razr_col))


def simplex(A, b, c, min=True):
    A_new = A.copy();
    A_new = np.concatenate((A_new,b),axis=1)
    function_row = c.copy()
    function_row.resize([1, A_new.shape[1]], refcheck=False)
    function_row = function_row * -1
    A_new = np.concatenate((A_new,function_row),axis=0)
    find_negative(A_new[:,A_new.shape[1]-1])
    basic_plan = find_basic_plan(A_new)
    if basic_plan is None:
        print('No basic plan')
        return
    
    while check_negative(A_new[A_new.shape[0]-1,:].A1):
        razr_column = -1

        #TODO use function
        for index, element in np.ndenumerate(A_new[A_new.shape[0]-1,:]):
            index = index[1]
            if element > 0:
                razr_column = index
                break
        if razr_column == -1:
            return A_new[A_new.shape[0]-1,:].A1
        number = -1
        min_number = number
        razr_row = -1
        #TODO use function
        for index, element in np.ndenumerate(A_new[:, razr_column]):
            index = index[0]
            if element > 0 and index != A_new.shape[0] - 1:
                number = A_new.item(index, A_new.shape[1] - 1)/element
                if (number < min_number or min_number == -1):
                    min_number = number
                    razr_row = index
        if razr_row == -1:
            print('Infinite function')
            return
        A_new = jordan(A_new,razr_row,razr_column)
    return A_new[:,A.shape[1]-1]



