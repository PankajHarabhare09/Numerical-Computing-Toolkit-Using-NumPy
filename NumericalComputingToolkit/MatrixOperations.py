import numpy as np
class MatrixOperations:

    def create_matrix(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        
        print("Enter Elements of the matrix(Row-Wise):")
        elements = []
        for i in range(rows):
            row = list(map(float , input().split()))
            elements.append(row)

        return np.array(elements)
    
    def add(self , a , b):
        return np.add(a , b)
    
    def subtract(self , a , b):
        return np.subtract(a , b)
    
    def multiply(self , a , b):
        return np.dot(a , b) #The numpy.dot() function in Python computes the dot product of two arrays
    
    def transpose(self , a):
        return np.transpose(a)
    
    def determinant(self , a):
        return np.linalg.det(a) #linear algebra operations
    
    def inverse(self , a):
        return np.linalg.inv(a) #linear algebra operations

