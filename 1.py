y = 2
x = 1
print(x+y)
smallest = []
while x<=10 :
    number = int(input(f' {x}enter a numberb: '))
    smallest.append(number)
    x+=1

#print(smallest)
smallest.sort()
print('kochak tarin add', smallest[0], 'ast')
#print('bozorg  tarin add', smallest[-1], 'ast')


for i in range(1,50,2):
    print(i)


x = 1
numbers = []
while x<=10 :
    number = int(input('nomrat ro vared kon '))
    numbers.append(number)
    x+=1

sum_1 = sum(numbers)
len_1 = len(numbers)
average = sum_1/len_1
print('moadel shoma brabare %i ast'  % average)


string = 'maliheh'
lst = []
for s in string:
    lst.append(s)
lst.reverse()    
#print(lst)
str_1=''
for l in lst:
    str_1 += l

print(string,'>>',str_1)







