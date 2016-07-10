import time
line_number = 0
'''
with open('leKernelTrain2Kx2K.txt') as train_file:
    arr = []
    start = time.time()
    for line in train_file:
        #print "digit digit example example  kernel-matrix-element"
        line_arr = line.split()
        if line_arr[0] == '1' and line_arr[2] == "1":
            #print "here"
            arr.append(line_arr[4])
    print arr
    f = open('precomputed_kernel', 'w')
    f.write('1 0:' + line_arr[0])
    count = 1
    for element in arr:
        f.write(" " + str(count) + ":" + element)
        count = count + 1
    end = time.time()
    print (end - start)

everything = []
# digit digit example example kernel_value
# i = 200c + l
everything.append(line_arr)
'''
'''
train example 1 : all 1s   1 -> 200
train example 1 : all 2s   40001 -> 40200

given the number of the training example, calculate all the index for the kernel values
for example: pass in training example #1
should return 1->200, 40001->40200, 80001->80200
# 2
return 201->400, 40201->40400, 80201->80400'
first 2 digit
train example 201 : all 1s 400001 -> 400200
train example 202 : all 2s 440001 -> 440200
'''
def getIndex(digit, n):
    tmp = []
    for c in range(0, 10):
        for l in range(1, 201):
            i = 40000 * c + (l + (n-1) * 200) + (digit-1) * 400000
            tmp.append(i)
    return tmp
everything = []
with open('leKernelTrain2Kx2K.txt') as train_file:
    for line in train_file:
        everything.append(line.split())
f = open('precomputed_kernel_final', 'w')
# Loop through digits
#for d in range(1, 11):
for d in range(1, 11):
    # Loop through nth examples in that class
    for n in range(1, 201):
        write_line = ''
        if d == 10:
            write_line = write_line + (str(0) + ' ' + '0:' + str(n+(d-1)*200))
        else:
            write_line = write_line + (str(d) + ' ' + '0:' + str(n+(d-1)*200))
        position = getIndex(d, n)
        index = 1
        for p in position:
            write_line = write_line + ' ' + str(index) + ':' + everything[p-1][4]
            index = index + 1
        write_line = write_line + '\n'
        f.write(write_line)
# param is the digit and nth in that digit class
# for example 1, 1
