f = open('precomputed_kernel_final_35', 'w')
# "3 0:1 1: .... 200:"
# "5 0:201 1.... 200:"
with open('leKernelTrain2Kx2K.txt') as train_file:
    count = 1
    write_line = "3 0:1"
    first_time = True
    for line in train_file:
        tmp = line.split()
        if tmp[0] == "3" and tmp[1] == "5":
            print tmp
            if count <= 200:
                write_line = write_line + " " + tmp[3] + ":" + tmp[4]
                count = count + 1

                print "<=200 " + tmp[3]
            else:
                f.write(write_line + '\n')
                count = 2
                write_line = "3 0:" + tmp[2]
                write_line = write_line + " " + tmp[3] + ":" + tmp[4]
                print "else" + tmp[3]
        elif tmp[0] == "5" and tmp[1] == "3":
            print tmp
            if first_time:
                first_time = False
                count = 1
                write_line = "5 0:201"
            if count <= 200:
                write_line = write_line + " " + tmp[3] + ":" + tmp[4]
                count = count + 1
            else:
                f.write(write_line + '\n')
                count = 2
                write_line = "5 0:" + str(int(tmp[2]) + 200)
                write_line = write_line + " " + tmp[3] + ":" + tmp[4]





