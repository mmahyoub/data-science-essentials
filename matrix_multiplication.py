'''
- Matrix multiplication is fundamental in linear algebra and widely used in data science.
- Applications include:
    - Multiplying input data matrix and layer weights in neural networks.
    - Projecting data into lower dimensions, as done in principal component analysis (PCA).
    - Solving systems of linear equations in optimization problems (multiplying augmented matrix by elimination matrices).
    - Implementing various machine learning algorithms such as linear regression and support vector machines.
    - Performing transformations in image processing.
    - And many more...

Here we examine common forms of matrix multiplication (AB = C), A, B, C are matrices; A is  m * n, B is n * p and C is m * p:
1. Row times column: Entity c_ij is the dot product of row i of matrix A and column j of matrix B.
2. Columns: Columns of C are linear combinations of columns of A.
3. Rows: Rows of C are linear combinations of rows of B.
4. Column times a row: C is the sum of the "column of A times row of B" matrices (for all corresponding columns and rows). 
'''
import numpy as np 

def main():
    A = np.array([[3,4], [5,2]])
    B = np.array([[1,3], [3,2]])
    
    # Multiplication using numpy for validation 
    C = np.matmul(A,B)
    print(f'Validation using Numpy:\n {C}')

    # Way 1: Row times column
    C = row_times_column(A, B)
    print(f'Method 1 - row times column:\n {C}')

    # Way 2: Columns 
    C = columns(A,B)
    print(f'Method 2 - columns:\n {C}')

    # Way 3: Rows
    C = rows(A,B)
    print(f'Method 3 - rows:\n {C}')

    # Way 4: Column times row
    C = column_times_row(A,B)
    print(f'Method 4 - column times row:\n {C}')

def row_times_column(A,B):
    '''
    Arguments:
        A: numpy array (m * n)
        B: numpy array (n * p)
    Returns:
        - C : numpy array (m * p)
    '''
    C = np.zeros(shape=(A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            C[i,j] = np.dot(A[i, :], B[:,j])  # Dot product of row i of matrix A and column j of matrix B will give us entity c_ij in matrix C
    return C

def columns(A,B):
    '''
    Arguments:
        A: numpy array (m * n)
        B: numpy array (n * p)
    Returns:
        - C : numpy array (m * p)
    '''
    C = np.zeros(shape=(A.shape[0], B.shape[1]))
    n = A.shape[1]
    for c in range(n):
        # Compute columns of C
        for r in range(n):
            C[:,c] += B[r,c] * A[:,r]   # Computing linear combinations of columns of A such that C[:,0] = B[0,0] * A[:,0] + B[1,0] * A[:,1] + ... + B[n,0] * A[:,n]
    return C

def rows(A, B):
    '''
    Arguments:
        A: numpy array (m * n)
        B: numpy array (n * p)
    Returns:
        - C : numpy array (m * p)
    '''
    C = np.zeros(shape=(A.shape[0], B.shape[1]))
    n = B.shape[0]
    for r in range(n):
        # Compute rows of C
        for c in range(n):
            C[:,r] += B[c,r] * A[:,c]   # Computing linear combinations of rows of B such that C[0,:] = A[0,0] * B[0,:] + A[0,1] * B[1,:] + ... + A[0,n] * B[n,:]
    return C

def column_times_row(A,B):
    '''
    Arguments:
        A: numpy array (m * n)
        B: numpy array (n * p)
    Returns:
        - C : numpy array (m * p)
    '''
    C = np.zeros(shape=(A.shape[0], B.shape[1]))
    n = A.shape[1]
    for i in range(n):
        # Multiply each column of A with row of B, will result in a matrix. Add all matrices --> C.
        C = C + np.outer(A[:,i], B[i,:])
    return C

if __name__ == "__main__":
    main()