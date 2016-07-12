import numpy as np
import math
K = []
for i in range(0, 2000):
    K.append([0] * 2000)
label = []
m_arr = []
for i in range(0, 2000):
    m_arr.append([0]*784)
with open('2000mnist') as mnist_file:
    index = 0
    for line in mnist_file:
        tmp = line.split()
        label.append(tmp[0])
        for e in tmp[1:]:
            tmp2 = e.split(':')
            m_arr[index][int(tmp2[0])-1] = float(tmp2[1])
        index = index + 1
print m_arr

for i in range(0, 2000):
    for j in range(0, 2000):
        K[i][j] = math.pow(np.dot(np.array(m_arr[i]), np.array(m_arr[j])) + 1, 2)

f = open('quadric_kernel','w')
for i in range(0, 2000):
    write_line = ''
    write_line = write_line + str(label[i]) + ' ' + '0:'+ str(i+1)
    for j in range(0, 2000):
        write_line = write_line + ' ' + str(j+1) + ':' + str(K[i][j])
    write_line = write_line + '\n'
    f.write(write_line)
