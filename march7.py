'''string match
txt=input()
pat=input()
m=len(txt)
n=len(pat)

for i in range(m-n+1):
    for j in range(0,len(pat)):
        if(txt[i+j]!=pat[j]):
            j-=1
            break
    #print(i,j)
    if(j==n-1):
        print("string found at",i)
'''

