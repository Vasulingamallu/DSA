'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(0)
second=Node(1)
third=Node(2)
head.next=second
second.next=third
def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def insert_at_position(head,data,pos):
    new_node=Node(data)
    temp=head
    if head==None:
        return new_node
    if pos==0:
        return insert_begin(head,data)
    flag=0
    while flag!=pos-1 :
        temp=temp.next
        flag+=1
    new_node.next=temp.next
    temp.next=new_node
    return head
#delete operations 
def delete_begin(head):
    if head is None:
        return None
    return head.next
def delete_end(head):
    if head is None or head.next is None:
        return None
    
    temp = head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
def delete_value(head,val):
    if head is None:
        return None
    if head.data == val:
        return head.next
    temp=head
    while temp.next and temp.next.data!=val:
        temp=temp.next
    if temp.next:
        temp.next=temp.next.next
    return head
#search
def search(head,val):
    temp=head
    pos=0
    while temp:
        if temp.data==val:
            return pos
        pos+=1
        temp=temp.next
    return -1
#reverse the linked list
def reverse(head):
    prev=None
    cur=head
    while cur:
        next_node=cur.next
        cur.next=prev
        prev=cur
        cur=next_node
    return prev
        
        
def display(head):

    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("NULL")
temp=head
temp=insert_begin(temp,56)
temp=insert_end(temp,65)
temp=insert_at_position(temp,55,1)
temp=insert_at_position(temp,54,2)

display(temp)
temp = delete_value(temp,0)
print("the position is found:",search(temp,54))
display(temp)
temp=reverse(temp)
display(temp)


        
