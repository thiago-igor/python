def dist_manhattan(a, b):
    maximo = 0
    
    for i in range(len(a)):
        sub = abs(A[i] - B[i])
        res = sub
        if(maximo <= res):
            maximo  = res  
    return maximo


A = [1, 3, 4, 5, 10]
B = [2, 11, 8, 9, 15]

print(dist_manhattan(A, B))