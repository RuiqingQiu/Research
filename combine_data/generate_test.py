number_of_digits = [15,10,10,10,10,10,10,10,10,10]
for i in range(0, 10):
    for j in range(i, 10):
        f = open('K_'+str(i)+'vs'+str(j)+'.txt', 'w')
        for k in range(0, number_of_digits[i]):
            for z in range(0, number_of_digits[j]):
                f.write(str(i) + str(j) + str(k) + str(z) + ' ')
            f.write('\n')

