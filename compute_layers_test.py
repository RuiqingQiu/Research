import time
import math

everything = []
with open('leKernelTrain2Kx2K.txt') as train_file:
    #index = 0
    for line in train_file:
        everything.append(line.split())
     #   index = index + 1
      #  if index == 200:
       #     break

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
        i = (10 - 1) * 200 + ei - 1
    else:
        i = (di - 1) * 200 + ei - 1
    j = 0
    if dj == 0:
        j = (10 - 1) * 200 + ej - 1
    else:
        j = (dj - 1) * 200 + ej - 1
    K[i][j] = k

label = []
with open('mnist.scale.t') as label_file:
    for line in label_file:
        label.append(line[0])

D = []
with open('leKernelTestDiag10K.txt') as diag_file:
    for line in diag_file:
        D.append(float(line.split()[0]))
print D
L = []
for i in range(0, 10000):
    L.append([0]*2000)

with open('leKernelTest2Kx10K.txt') as test_file:
    for line in test_file:
        tmp = line.split()
        di = int(tmp[0])
        ei = int(tmp[1])
        i = 0
        if di == 0:
            i = (10-1)*200 + ei -1
        else:
            i = (di-1)*200 + ei -1
        j = int(tmp[2]) - 1
        L[j][i] = float(tmp[3])

Ll = []
for i in range(0, 10000):
    Ll.append([0] * 2000)
for j in range(0, 10000):
    for i in range(0, 2000):
        val = math.sqrt(K[i][i] * D[j])
        cos = L[j][i] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        Ll[j][i] = (1/math.pi) * val * (sin + (math.pi-theta)*cos)
f = open('precomputed_kernel_1_layer_test','w')
for j in range(0, 10000):
    print j
    write_line = ''
    write_line = write_line + (label[j] + ' ' + '0:' + str(j+1))
    for i in range(0, 2000):
        write_line = write_line + ' ' + str(i+1) + ':' + str(Ll[j][i])
    write_line = write_line + '\n'
    f.write(write_line)

def next_layer(K):
    Kl = []
    for i in range(0, 2000):
        Kl.append([0]*2000)
    for i in range(0, 2000):
        for j in range(0,2000):
            val = math.sqrt(K[i][i] * K[j][j])
            cos = K[i][j] / val
            theta = math.acos(cos)
            sin = math.sqrt(1 - cos * cos)
            Kl[i][j] = (1/math.pi) * val * (sin + (math.pi - theta) * cos)
    return Kl
'''

K2 = next_layer(K)
K3 = next_layer(K2)
K4 = next_layer(K3)

L3 = []
for i in range(0, 10000):
    L3.append([0] * 2000)
for j in range(0, 10000):
    for i in range(0, 2000):
        val = math.sqrt(K2[i][i] * D[j])
        cos = Ll[j][i] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        L3[j][i] = (1/math.pi) * val * (sin + (math.pi - theta) * cos)

f = open('precomputed_kernel_2_layer_test', 'w')
for j in range(0, 10000):
    write_line = ''
    write_line = write_line + (label[j] + ' ' + '0:' + str(j+1))
    for i in range(0, 2000):
        write_line = write_line + ' ' + str(i+1) + ':' + str(L3[j][i])
    write_line = write_line + '\n'
    f.write(write_line)


L4 = []
for i in range(0, 10000):
    L4.append([0] * 2000)
for j in range(0, 10000):
    for i in range(0, 2000):
        val = math.sqrt(K3[i][i] * D[j])
        cos = L3[j][i] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        L4[j][i] = (1/math.pi) * val * (sin + (math.pi - theta) * cos)

f = open('precomputed_kernel_3_layer_test', 'w')
for j in range(0, 10000):
    write_line = ''
    write_line = write_line + (label[j] + ' ' + '0:' + str(j+1))
    for i in range(0, 2000):
        write_line = write_line + ' ' + str(i+1) + ':' + str(L4[j][i])
    write_line = write_line + '\n'
    f.write(write_line)

L5 = []
for i in range(0, 10000):
    L5.append([0] * 2000)
for j in range(0, 10000):
    for i in range(0, 2000):
        val = math.sqrt(K4[i][i] * D[j])
        cos = L4[j][i] / val
        theta = math.acos(cos)
        sin = math.sqrt(1 - cos * cos)
        L5[j][i] = (1/math.pi) * val * (sin + (math.pi - theta) * cos)

f = open('precomputed_kernel_4_layer_test', 'w')
for j in range(0, 10000):
    write_line = ''
    write_line = write_line + (label[j] + ' ' + '0:' + str(j+1))
    for i in range(0, 2000):
        write_line = write_line + ' ' + str(i+1) + ':' + str(L5[j][i])
    write_line = write_line + '\n'
    f.write(write_line)
'''
