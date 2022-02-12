from math import hypot
import os


with open('maps/map.txt', 'r')as f:
    a = f.readlines()
# print(a[0].split(' ')[2][:-1])

# left is 1

left_cones = []
right_cones = []

for i in a:
    t = i.split(' ')
    if t[2][:-1] == '1':
        left_cones.append([t[0], t[1]])
    else:
        right_cones.append([t[0], t[1]])
# print(len(left_cones))
cone = []
txt = []
s = ""
for i in left_cones:
    cone.append([str(round(float(i[0]), 2)), str(round(float(i[1]), 2)), '1'])
    s += str(round(float(i[0]), 2))+' '+str(round(float(i[1]), 2))+' '
    ss = s + '1\n'
    txt.append(ss)
    # print(ss)
    for j in right_cones:
        flag = False
        for t in cone:
            if hypot(float(t[0])-float(j[0]), float(t[1])-float(j[1]))<=5:
                flag = True
                break
        if flag == True:
            ss = s + str(round(float(j[0]), 2))+' '+str(round(float(j[1]), 2))+' 0\n'
            txt.append(ss)
# print(hypot(4,3))

with open('out.txt', 'w') as f:
    print(len(txt))
    for i in txt:
        if len(i) < 30:
            continue
        f.writelines(i)