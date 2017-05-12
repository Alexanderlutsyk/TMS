Matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(i):
        temp = Matrix[i][j]
        Matrix[i][j] = Matrix[j][i]
        Matrix[j][i] = temp
print(Matrix)
