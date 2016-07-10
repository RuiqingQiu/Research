import time
import math

def getIndex(digit, n):
    tmp = []
    for c in range(0, 10):
        for l in range(1, 201):
            i = 40000 * c + (l + (n-1) * 200) + (digit-1) * 400000
            tmp.append(i)
    return tmp
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
    print "i : " + str(i) + ", j : " + str(j)
    K[i][j] = k

Kl = []
for i in range(0, 2000):
    Kl.append([0] * 2000)
for i in range(0, 2000):
    for j in range(0, 2000):
        val = math.sqrt(K[i][i] * K[j][j])
        cos = K[i][j] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        Kl[i][j] = (1/math.pi) * val * (sin + (math.pi-theta)*cos)

f = open('precomputed_kernel_1_layer','w')
for i in range(0, 2000):
    print i
    write_line = ''
    if i/200 == 9:
        write_line = write_line + (str(0) + ' ' + '0:' + str(i+1))
    else:
        write_line = write_line + (str(i/200 + 1) + ' ' + '0:' + str(i+1))
    for j in range(0, 2000):
        write_line = write_line + ' ' + str(j+1) + ':' + str(Kl[i][j])
    write_line = write_line + '\n'
    f.write(write_line)
'''
K2 = []
for i in range(0, 2000):
    K2.append([0] * 2000)
for i in range(0, 2000):
    for j in range(0, 2000):
        val = math.sqrt(Kl[i][i] * Kl[j][j])
        cos = Kl[i][j] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        K2[i][j] = (1/math.pi) * val * (sin + (math.pi-theta)*cos)

f = open('precomputed_kernel_2_layer', 'w')
for i in range(0, 2000):
    write_line = ''
    if i/200 == 9:
        write_line = write_line + (str(0) + ' ' + '0:' + str(i+1))
    else:
        write_line = write_line + (str(i/200 + 1) + ' ' + '0:' + str(i+1))
    for j in range(0, 2000):
        write_line = write_line + ' ' + str(j+1) + ':' + str(K2[i][j])
    write_line = write_line + '\n'
    f.write(write_line)


K3 = []
for i in range(0, 2000):
    K3.append([0] * 2000)
for i in range(0, 2000):
    for j in range(0, 2000):
        val = math.sqrt(K2[i][i] * K2[j][j])
        cos = K2[i][j] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        K3[i][j] = (1/math.pi) * val * (sin + (math.pi-theta)*cos)

f = open('precomputed_kernel_3_layer', 'w')
for i in range(0, 2000):
    write_line = ''
    if i/200 == 9:
        write_line = write_line + (str(0) + ' ' + '0:' + str(i+1))
    else:
        write_line = write_line + (str(i/200 + 1) + ' ' + '0:' + str(i+1))
    for j in range(0, 2000):
        write_line = write_line + ' ' + str(j+1) + ':' + str(K3[i][j])
    write_line = write_line + '\n'
    f.write(write_line)



K4 = []
for i in range(0, 2000):
    K4.append([0] * 2000)
for i in range(0, 2000):
    for j in range(0, 2000):
        val = math.sqrt(K3[i][i] * K3[j][j])
        cos = K3[i][j] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        K4[i][j] = (1/math.pi) * val * (sin + (math.pi-theta)*cos)

f = open('precomputed_kernel_4_layer', 'w')
for i in range(0, 2000):
    write_line = ''
    if i/200 == 9:
        write_line = write_line + (str(0) + ' ' + '0:' + str(i+1))
    else:
        write_line = write_line + (str(i/200 + 1) + ' ' + '0:' + str(i+1))
    for j in range(0, 2000):
        write_line = write_line + ' ' + str(j+1) + ':' + str(K4[i][j])
    write_line = write_line + '\n'
    f.write(write_line)




'''
