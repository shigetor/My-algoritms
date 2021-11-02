def Gauss():
    n = int(input("Введите количество переменных"))
    N = 0
    for i in range(n + 1):
        N = N + i;
    print(N)
    newArr = []
    print("Введите коэфф матрицы")
    for i in range(N):
        variable1 = int(input(f' {i} '))
        newArr.append(variable1)

    print("Введите коэффы")
    newArr1 = []
    for i in range(n):
        variable2 = int(input(f' {i} '))
        newArr1.append(variable2)
    print(newArr)
    print(newArr1)
    num = -1
    for i in range(n):
        num = num + 1
        x = (i * (i + 1)) / 2 + num
        newArr1[i] = newArr1[i] / newArr[x]
        newArr[x] = 1
        for j in range(n):
            y = (j * (j + 1)) / 2 + num
            newArr1[j] = newArr[j] - newArr1[i] * newArr[y]
            newArr[y] = 0
    for i in range(n):
        print(f'x{i + 1} = {newArr1[i]}\t')


a = Gauss()
print(a)
import time
startTime = time.time()

endTime = time.time()
totalTime = endTime - startTime