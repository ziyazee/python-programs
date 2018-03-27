'''exp = "a+b*(c^d-e)^(f+g*h)-i"
print(len(exp))
i=1
while(not i):
    print(i)

ch="+"
print(ch.isalpha())

class convo:
    def __init__(self,exp):
        self.top=-1
        self.capacity=exp
        self.array=[]
        self.output=[]
        self.precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def isEmpty(self):
        if(self.top==-1):
            return True
        return False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if(not self.isEmpty()):
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self,ch):
        self.top +=1
        self.array.append(ch)
    def isOperand(self,ch):
        return ch.isalpha()
    def infix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i=='(':
                self.push(i)
            elif i==')':
                while( not self.isEmpty()) and self.peek()!='(':
                    if self.isOperand(i):



exp="a+b+c"
r=convo(len(exp))





case = int(input())
for i in range(case):
    st = input()
    s = st.lower()
    s+="/"
    #print(len(s)-2)
    t=1
    a=[]
    for i in range(len(s)-1):
        if s[i]!=s[i+1] or i ==len(s)-2:
            print(s[i+1])
            if s[i]==s[i+1] and i==len(s)-2:
                t+=1
            a.append(str(t)+s[i])
           # print(str(t)+s[i])
            t=1
        else:
            t+=1
            #print("t=",t)
            continue
    #print(t)
    print("".join(a))

'''


















''' success
b=int(input())
for i in range(b):
    a=input()
    s=a.lower()
    s+="/"
    t=1
    b=[]
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            t+=1
            continue;

        b.append(str(t)+s[i])
        t = 1
    print("".join(b))

'''


'''success
b=int(input())

for i in range(b):
    a=input()
    bb=[]
    output=[]
    c=0
    for j in range(len(a)):

        if(a[j]=='('):

            c+=1

            bb.append(str(c))
            output.append(str(c))
            continue
        elif(a[j]==')'):
            z = c
            output.append(bb.pop())

            z-=1
            continue
        else:
            continue
    print("".join(output))
'''
t=int(input())
for i in range(t):
 n=int(input())
 sum=0
 aa=[]
 aa= [int(x) for x in input().split()]

#aa.append(bb[0])
 for i in range(0,n):
    for j in range(i+1,n):
        if(aa[j]>aa[i]):
            sum+=aa[j]

            break

 print(sum%1000000001)
#for i in range(n):
 #   if









