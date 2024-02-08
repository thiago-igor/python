list = [10, 5, 8, 12, 2]
n = len(list)

for j in range(1, n):
    chave = list[j]
    i = j - 1
    while(i >= 0 and list[i] > chave):
        list[i + 1] = list [i]
        i = i -1
    list[i + 1] = chave
    print(list)
