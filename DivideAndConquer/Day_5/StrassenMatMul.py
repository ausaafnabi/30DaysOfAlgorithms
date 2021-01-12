import numpy as np

def split(matrix):
    '''
    Splits a matrix into 4 sections(quarters)
    '''
    row,col = matrix.shape
    row2,col2 = row//2,col//2
    return matrix[:row2,:col2],  matrix[:row2,col2:],  matrix[row2:,:col2],  matrix[row2:,col2:] 

def strassen(x,y):
    '''
    Computes matrix product by DAC
    '''

    if len(x) == 1:
        return x*y

    a,b,c,d = split(x)
    e,f,g,h = split(y)

    # computing 7 products, recursively
    #
    p1 = strassen(a,f-h)
    p2 = strassen(a+b,h)
    p3 = strassen(c+d,e)
    p4 = strassen(d,g-e)
    p5 = strassen(a+d,e+h)  
    p6 = strassen(b-d,g+h)
    p7 = strassen(a-c,e+f)

    # computing 4 quadrants
    #
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combining 4 quadrants into single
    # by stacking horizontally
    c = np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))

    return c

def main():
    a = np.matrix([[2,2],[2,2]])
    b = np.matrix([[3,2],[2,3]])
    print(a,"\n * \n",b)
    c = strassen(a,b)
    print()
    print(c)

if __name__ == "__main__":
    main()


