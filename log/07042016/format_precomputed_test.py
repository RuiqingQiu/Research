import time
line_number = 0

'''
test example 1: K(x, x1) ... K(x,x200)
1
10001
20001
...
19990001
'''
# The nth test point
def getIndex(n):
    tmp = []
    for l in range(0, 2000):
        i = n + l*10000
        tmp.append(i)
    return tmp
everything = []
label = []
with open('mnist.scale.t') as label_file:
    for line in label_file:
        label.append(line[0])
with open('leKernelTest2Kx10K.txt') as train_file:
    # f.write("7 0:?")
    for line in train_file:
        tmp = line.split()
        everything.append(tmp)
f = open('precomputed_kernel_test_final', 'w')

for i in range(1, 10001):
    print i
    f.write(label[i-1] + " 0:0")
    position = getIndex(i)
    index = 1
    for p in position:
        f.write(" " + str(index) + ":" + everything[p-1][3])
        index = index + 1
    f.write('\n')

'''
f = open('precomputed_kernel_final', 'w')
# Loop through digits
for d in range(1, 11):
    # Loop through nth examples in that class
    for n in range(1, 201):
        print n
        print d
        f.write(str(d) + " " + "0:" + str(n+(d-1)*200))
        position = getIndex(d, n)
        index = 1
        for p in position:
            f.write(" " + str(index) + ":" + everything[p-1][4])
            index = index + 1
        f.write('\n')
'''
# param is the digit and nth in that digit class
# for example 1, 1
