num = [2 , -3 , 0 , 4 , -5 , 1, -1 , 6]
num.sort()
print(num)
n_num_pos = []
n_num_neg = []
for i in num:
    if i > 0 :
        n_num_pos.append(i)
    if i < 0 :
        n_num_neg.append(i)
n_num_neg.reverse()
n_num_neg.extend(n_num_pos)
print(n_num_neg)

print(n_num_neg[0:3])