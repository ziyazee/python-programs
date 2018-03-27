'''

t=int(input())
for i in range(t):
    n=int(input())
    a=[]

      #  print(j)
    a=input().split()
    a.sort()
    a.reverse()
    print(a[0])
    print(a[1])
    print(int(a[0])+int(a[1]))
'''
'''
#code
t=int(input())
z=0
while z<t:
    b=[]
    n=int(input())
    a=input().split()
    b.append(a[0])
   # print(b[-1])
    for i in range(1,len(a)):
       # print(i)


        if(b and a[i]==b[-1]):
            b.pop()
            #print("popped")
            #print(a[-1])
        else:
            #print("pushed",a[i])
            b.append(a[i])

    print(len(b))
    z+=1
'''




#google problem din solve
t=int(input())
z=0

while z<t:

    s=input().strip()
    a=[]
    c=0
    
    for i in range(0,len(s)):
        if(s[i]=="("):
            a.append(s[i])
            print("pushed",i)
            continue
        else:
             if(a):
             #   print("hy")
                a.pop()
                print("popped",i)
                c+=2
               # print(c)
    
    print(c)
    z+=1
    



#d="fgg"
#for i, e in enumerate(d):
 #   print(i)

'''def solve(parenthesis):
    stack = []
    cur = 0
    ret = 0
    for i, e in enumerate(parenthesis):
        if e == '(':
            stack.append(cur)
            cur = 0
            print(stack,i)
        elif e == ')' and len(stack) > 0:
            cur += stack.pop() + 2
            ret = max(ret, cur)
        elif e == ')' and len(stack) == 0:
            cur = 0
    return ret


t=int(input())
while t>0:
    parenthesis=input()
    print(solve(parenthesis))
    t=t-1
    
'''