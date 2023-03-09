import math
def dist_euclidiana(a, b):
    soma = 0
    
    for i in range(len(a)):
        sub = a[i] - b[i]
        soma += math.pow(sub, 2)
    
    return math.sqrt(soma)

A = [10,1,3,12]
B = [4,5,4,2]

print(dist_euclidiana(A, B))