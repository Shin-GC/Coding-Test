count=0
number=str([x for x in range(1,10000+1)])
for i in range(len(number)):
    if number[i]=='8':
       count+=1
print(count)

print(str(list(range(1,10000+1))).count('8'))