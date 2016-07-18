import math
everything = []
with open('leKernelTrain2Kx2K.txt') as train_file:
    #index = 0
    for line in train_file:
        everything.append(line.split())
        #index = index + 1
        #if index == 400:
            #break

# param is the digit and nth in that digit class
# for example 1, 1
K = []
for i in range(0, 2000):
    K.append([0] * 2000)
for element in everything:
    di = int(element[0])
    dj = int(element[1])
    ei = int(element[2])
    ej = int(element[3])
    k = float(element[4])
    i = 0
    if di == 0:
        i = (10 - 1)*200 + ei - 1
    else:
        i = (di - 1) * 200 + ei - 1
    j = 0
    if dj == 0:
        j = (10 - 1)*200 + ej - 1
    else:
        j = (dj - 1) * 200 + ej - 1
    K[i][j] = k

def trace(K):
    sum = 0.0
    for i in range(0, 2000):
        sum = sum + K[i][i]
    return sum
def allSum(K):
    sum = 0.0
    for i in range(0, 2000):
        for j in range(0, 2000):
            sum = sum + K[i][j]
    #sum = sum / 2000
    return sum

t = trace(K)
t = t / 2000
sum1 = allSum(K)
sum1 = sum1/ (2000*2000)
C = 1 / abs(t - sum1)
print C * math.pow(2,-10)
print C * math.pow(2,-9)
print C * math.pow(2,-8)
print C * math.pow(2,-7)
print C * math.pow(2,-6)
print C * math.pow(2,-5)
print C * math.pow(2,-4)
print C * math.pow(2,-3)
print C * math.pow(2,-2)
print C * math.pow(2,-1)
print C * math.pow(2, 0)
print C * math.pow(2, 1)
print C * math.pow(2,2)
print C * math.pow(2,3)
print C * math.pow(2,4)
print C * math.pow(2,5)
print C * math.pow(2,6)
print C * math.pow(2,7)
print C * math.pow(2,8)
print C * math.pow(2,9)
print C * math.pow(2,10)









