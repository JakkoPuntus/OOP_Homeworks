a=input()
a_list =list(map(int,input().split()))
b=input()
b_list =list(map(int,input().split()))
c=input()
c_list =list(map(int,input().split()))
cnt=0

l = a_list + b_list + c_list
l.sort()

for i in range(len(l)-2):
    if l[i] == l[i+1] == l[i+2]:
        cnt += 1

print(cnt)