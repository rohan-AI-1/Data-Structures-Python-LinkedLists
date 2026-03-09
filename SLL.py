class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def IATFRONT(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(self.head.data,"is inserted at front")
        else:
            newnode.next=self.head
            self.head=newnode
            print(self.head.data,"is inserted at front")
    def IATEND(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            print(self.head.data,"is inserted at the End")
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            print(temp.next.data,"is inserted at End")
    def DELETEATFRONT(self):
        if self.head is None:
            print("List is empty.Cant delete")
        elif self.head.next is None:
            print(self.head.data,"is Deleted from front")
            self.head=None
        else:
            print(self.head.data,"is Deleted from front")
            self.head=self.head.next
    def DELETEATEND(self):
        if self.head is None:
            print("List is Empty.Cant delete")
        elif self.head.next==None:
            print(self.head.data,"is Deleted from front")
            self.head=None
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            print(temp.next.data,"is Deleted from End")
            temp.next=None
    def DISPLAY(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,"->",end=" ")
                temp=temp.next
            print("None")
    def COUNTNODES(self):
        count=0
        if self.head is None:
            print("List is Empty.")
        else:
            temp=self.head
            while temp!=None:
                count=count+1 
                temp=temp.next
            print("The total number of nodes in the list =",count)
Obj=LinkedList()
while True:
    ch=int(input("Singly Linked List Menu\n1.Insert at Front\n2.Insert at End\n3.Delete at Front\n4.Delete from End\n5.Display\n6.Count\n7.Exit\nEnter your choice:"))
    if ch==1:
        n=int(input("Enter data value:"))
        Obj.IATFRONT(n)
    elif ch==2:
        n=int(input("Enter data value:"))
        Obj.IATEND(n)
    elif ch==3:
        Obj.DELETEATFRONT()
    elif ch==4:
        Obj.DELETEATEND()
    elif ch==5:
        Obj.DISPLAY()
    elif ch==6:
        Obj.COUNTNODES()
    elif ch==7:
        break
    else:
        print("Invalid Choice")
