class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
n1=node(2)
n2=node(4)
n3=node(3)
l1=node(5)
l2=node(6)
l3=node(4)
carry=0
n1.next=n2
n2.next=n3
l1.next=l2
l2.next=l3
current=n1
current2=l1
a=[]
r1=None
r2=None
r3=None
for i in range(3):
    if carry==0:
        d=current.data+current2.data
    else:
        d=current.data+current2.data+carry
    if d<10:
        r3=node(d)
    else:
        r3=node(d%10)
        carry=int(d/10)
    a.append(r3.data)
    if (r1==None):
        r1=r3
    elif r2==None:
        r2=r3
    else:
        pass
    current=current.next
    current2=current2.next
r1.next=r2
r2.next=r3

print(a)