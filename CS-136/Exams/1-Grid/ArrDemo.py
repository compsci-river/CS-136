
# First method to create a 2D array 
rows, cols = (5, 5)
arr1 = [[0]*cols]*rows 
print("2D Array, initialized by method 1:")
for row in arr1: 
    print(row)


# Second method to create a 2D array 
rows, cols = (5, 5) 
arr2 = [[0 for i in range(cols)] for j in range(rows)] 
print("2D Array, initialized by method 2:")
for row in arr2: 
    print(row) 

# Demonstrate working of method 1 and method 2. 
arr1[0][0] = 1
print("2D Array, value changed, method 1:")
for row in arr1: 
    print(row)

arr2[0][0] = 1
print("2D Array, value changed, method 2:")
for row in arr2: 
    print(row) 
