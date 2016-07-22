import time
fw = open('overall.txt', 'w')
# Digit A
start_time = time.time()
index = 1
for i in range(0, 10):
    #Number of examples
    f_arr = []
    for j in range(0, 10):
        if(i <= j):
            f = open('K_'+str(i)+'vs'+str(j)+'.txt','r')
            f_arr.append(f)
        else:
            f = open('K_'+str(j)+'vs'+str(i)+'.txt', 'r')
            f_arr.append(f)
    for k in range(0, 10):
        #write the label
        fw.write(str(i) + ' ' + '0:' + str(index) + ' ')
        index = index + 1
        matrix_index = 1
        #write all the matrix element
        for f in f_arr:
            tmp = f.readline().rstrip('\n')
            lst = tmp.split()
            for number in lst:
                fw.write(str(matrix_index) + ':' + number + ' ')
                matrix_index = matrix_index + 1
        fw.write('\n')
print("--- %s seconds ---" % (time.time() - start_time))
