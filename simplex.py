import numpy as np

#A = [[2,1,3,4],[1,-1,2,1],[0,0,1,3]]
#b = [[2],[4],[1]]
#c = [-2, 3, 4, -1]

A = np.matrix('2. 1 3 4; 1 -1 2 1; 0 0 1 3')
b = np.matrix('2; 4; 1')
c = np.matrix('-2 3 4 -1')


def simplex(A, b, c, min=True):
    A_new = A.copy();
    #A_new = np.matrix('2 1 3 4; 1 -1 2 1; 0 0 1 3')
    A_new = A.copy();
    A_new = np.concatenate((A_new,b),axis=1)
    function_row = c.copy()
    function_row.resize([1, A_new.shape[1]], refcheck=False)
    A_new = np.concatenate((A_new,function_row),axis=0)
    
    while True:
        razr_column = -1
        for index, element in np.ndenumerate(A_new[A_new.shape[0]-1,:]):
            index = index[1]
            if element > 0:
                razr_column = index
                break
        if razr_column == -1:
            return A_new[A_new.shape[0]-1,:]
        number = -1
        min_number = number
        razr_row = -1
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
        razr_element = A_new.item(razr_row, razr_column)
        A_old = A_new.copy()
        A_new.itemset((razr_row, razr_column), 1.0 / razr_element)
        for index, element in np.ndenumerate(A_old[:, razr_column]):
            index = index[0]
            if index == razr_row:
                continue
            A_new.itemset((index, razr_column), -
                      A_old.item(index, razr_column) / razr_element)
        for index, element in np.ndenumerate(A_old[razr_row, :]):
            index = index[1]
            if index == razr_column:
                continue
            A_new.itemset((razr_row, index), A_old.item(razr_row, index)/razr_element)
        for index, element in np.ndenumerate(A_old):
            if (index[0] == razr_row or index[1] == razr_column):
                continue
            new_element = A_old.item(index) - 1. * A_old.item(razr_row, index[1]) * \
                A_old.item(index[0], razr_column) / razr_element
            A_new.itemset(index, new_element)


print("Something")
print(simplex(A, b, c))
# print(type(A.shape))
# print(A[A.shape[0]-1])
