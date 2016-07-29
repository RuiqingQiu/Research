import time
# Digit A
start_time = time.time()
index = 1
number_of_digits = [15,10,10,10,10,10,10,10,10,10]
validate = [2,2,2,2,2,2,2,2,2,2]

for i in range(0, 10):
    f_arr = []
    for j in range(0, 10):
        f = open('K_'+str(i)+'vs'+str(j)+'.txt','r')
        f1 = open('trainK_'+str(i)+'vs'+str(j)+'.txt', 'w')
        f2 = open('validateK_'+str(i)+'vs'+str(j)+'.txt', 'w')
        k = 0
        for line in f:
            if k >= number_of_digits[i]-validate[i]:
                f2.write(str(i) + ' ' + '0:' + str(index) + ' ')
                matrix_index = 1
                #write all the matrix element
                lst = line.split()
                count = 1
                for number in lst:
                    if count > number_of_digits[j] - validate[j]:
                        f2.write(str(matrix_index) + ':' + number + ' ')
                        matrix_index = matrix_index + 1
                    count = count + 1
                f2.write('\n')

            else:
                f1.write(str(i) + ' ' + '0:' + str(index) + ' ')
                matrix_index = 1
                #write all the matrix element
                lst = line.split()
                count = 1
                for number in lst:
                    if count == number_of_digits[j] - validate[j] + 1:
                        break
                    else:
                        f1.write(str(matrix_index) + ':' + number + ' ')
                    count = count + 1
                    matrix_index = matrix_index + 1
                f1.write('\n')
            index = index + 1
            k = k + 1
print("--- %s seconds ---" % (time.time() - start_time))
