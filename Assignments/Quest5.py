N = int(input("Enter the Size for your matrices:")) 
  
matrix1 = [] 
print("Enter the entries for first matrix rowwise:") 
  

for i in range(N):          
    a =[] 
    for j in range(N):       
         a.append(int(input())) 
    matrix1.append(a) 



matrix2 = [] 
print("Enter the entries for second matrix rowwise:") 
  

for i in range(N):           
    a =[] 
    for j in range(N):       
         a.append(int(input())) 
    matrix2.append(a) 


for i in range(N): 
    for j in range(N): 
        print(matrix1[i][j], end = " ") 
    print() 

for i in range(N): 
    for j in range(N): 
        print(matrix2[i][j], end = " ") 
    print() 


add_matrix = []
for i in range(0,N):
  a = []
  for j in range(0,N):
    a.append(matrix1[i][j]+matrix2[i][j])
  add_matrix.append(a)
print("Addition of matrix is",add_matrix)

multi_matrix = []
for i in range(0,N):
  a = []
  for j in range(0,N):
    summ = 0
    for k in range(0,N):
      summ = summ+(matrix1[i][k]*matrix2[k][j])
    a.append(summ)
  multi_matrix.append(a)
print("Matrix1 x matrix 2 =",multi_matrix)


tr_matrix=[]

for i in range(0,N):
  a = []
  for j in range(0,N):

    a.append(matrix1[j][i])
  tr_matrix.append(a)

print("Transpose of matrix 1 is",tr_matrix)