count = 0
for i in range(0, 10):
    for j in range(0, 10):
        if i > j:
            arr = []
            f = open('K_'+str(i)+'vs'+str(j)+'.txt','w')
            f2 = open('K_'+str(j)+'vs'+str(i)+'.txt','r')
            print (f2)
            line_length = 0
            for line in f2:
                arr.append(line.split())
                line_length = len(line.split())
                print line_length
            for index in range(0, line_length):
                for element in arr:
                    f.write(element[index] + ' ')
                f.write('\n')



            count = count + 1
            #print ('K_'+str(i)+'vs'+str(j)+'.txt', 'w')
print count
