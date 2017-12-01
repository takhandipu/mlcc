import csv
import sys

j = 0 
data = {}

min = 0
max = 0
first = True

with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # data[j] = row
        data[j] = [float(row[0]), float(row[1]), 0]
        if first:
            first = False
            min = float(row[0])
            max = float(row[0])
            pass
        else:
            if min>float(row[0]):
                min = float(row[0])
                pass
            if max<float(row[0]):
                max = float(row[0])
                pass
            pass
        j+=1
        pass
    pass

timeCount = int(max-min)
sampleCount = int((max-min)*100)


min = data[0][0]
sum = 0
for i in range(j):
    data[i][0]-=min
    data[i][2]=sum+data[i][1]
    sum+=data[i][1]

bin = {}
for i in range(sampleCount):
    bin[i] = i * 1.0 / 100
    pass
results = {}

indexStart = 0
start = 0
for i in range(sampleCount):
    while (indexStart < j and data[indexStart][0]<=bin[i]):
        indexStart+=1
        pass
    if indexStart >= j:
        break
    value = data[indexStart][2] - data[indexStart][1] - start
    results[i] = value
    start += value

for i in range(sampleCount):
    print bin[i], ",", 
    if i in results:
        print int(results[i])
        pass
    else:
        print 0
    pass

