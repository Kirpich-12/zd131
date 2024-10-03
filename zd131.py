data_s =  open('input.txt', 'r')
data = data_s.read()
data_split = data.split()

dl = int(data_split[0]) * 2
# nunmders of people in house

num = 0
#number oldest men in house

sr = 0


for i in range(1, dl + 1, 2):
    if data_split[i+1] == '1':
        num = (i+1) // 2
        if int(data_split[num*2 - 1]) > sr:
            sr = num
print(sr)
data_s.close()

