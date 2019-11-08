from simplex import *


# A = np.matrix('2. 1 3 4; 1 -1 2 1; 0 0 1 3')
# b = np.matrix('2; 4; 1')
# c = np.matrix('-2 3 4 -1')

# A = np.matrix('2. 1 3 4; 1 -1 2 1; 0 0 1 3')
# b = np.matrix('2; 4; 1')
# c = np.matrix('-2 3 4 -1')

# A = np.matrix('2. 1 3 4; 1 -1 2 1; 0 0 1 3')
# b = np.matrix('2; 4; 1')
# c = np.matrix('-2 3 4 -1')

A = np.matrix('-1. 2; 1 1; 1 -1;0 1')
b = np.matrix('2; 4; 2; 6')
c = np.matrix('1 2')

# A = np.matrix('2. 3 1 2 1; 2 1 -3 2 1; 2 1 2 1 0')
# b = np.matrix('1; 3; 1')
# c = np.matrix('-1 1 -2 1 5')

# A = np.matrix('1. 1 ; 5 2 ')
# b = np.matrix('4; 10')
# c = np.matrix('5 3') #Must be [0.66, 3.33]

print('A= ',A)
print('b= ',b)
print('c= ',c)
plan = simplex(A, b, c)
print('Optimal plan: ', plan)
print('f(x) = ', func(c.A1,plan))
# print(type(A.shape))
# print(A[A.shape[0]-1])