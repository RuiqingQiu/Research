f = open('2000mnist', 'w')
counter = [0] * 10
with open('mnist.scale.t') as datafile:
    count = 0
    for line in datafile:
        if count >= 2000:
            break
        tmp = line.split()
        label = tmp[0]
        if(counter[int(label)] < 200):
            f.write(line)
            count = count + 1
            counter[int(label)] = counter[int(label)] + 1

