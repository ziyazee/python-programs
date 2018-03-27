class Queue:
        def __init__(self):
            self.items = []



        def enqueue(self, item):
            self.items.insert(0,item)


        def dequeue(self):
            if(not self.items == []):
                return self.items.pop()
            else:
                print("queue is empty")
        def size(self):
            return len(self.items)
        def pri(self):
            print(self.items)

        def f(self,x):
            {
                '1':print("1"),
                'b': 2,
            }
q=Queue()
i=1
while(i):
    print("enter the options u want")
    print("1:insert 2:delete 3:display 4:exit")
    ch=int(input())
   # dict['ch']
   # dict={'1':print("1"),'2':print("2")}
    def nqueue():
        print("enter item");
        xx=input()
        q.enqueue(xx)
    def g(x):
        {
            '1': nqueue(),
            'b': 2,
        }
    g(ch)

    q.enqueue(4)
    q.pri()
    q.enqueue('dog')
    q.pri()
    q.enqueue(5)
    q.pri()
    q.dequeue()
    q.pri()
    q.dequeue()
    q.pri()
    i-=1