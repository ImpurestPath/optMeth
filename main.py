from simplex import *


# A = np.matrix('2. 1 3 4; 1 -1 2 1; 0 0 1 3')
# b = np.matrix('2; 4; 1')
# c = np.matrix('-2 3 4 -1')


# A = np.matrix('2. 3 1 2 1; 2 1 -3 2 1; 2 1 2 1 0')
# b = np.matrix('1; 3; 1')
# c = np.matrix('-1 1 -2 1 5')

print('A= ',A)
print('b= ',b)
print('c= ',c)
preplan = simplex(A, b, c)
if not preplan is None:
    plan = preplan[:A.shape[1]]
    print('Optimal plan: ', plan)
    print('f(x) = ', func(c.A1,plan))

# print(type(A.shape))
# print(A[A.shape[0]-1])
