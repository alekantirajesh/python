# 17. Word Counter
# - Create a program to count the occurrences of each word in a sentence provided by the
# user.

sentence=input()

d={}
s=sentence.split(' ')
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)