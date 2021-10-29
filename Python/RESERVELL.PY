class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
def reverse(head):
    prev=None
    next=head
    curr=head
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head

def printLL(head):
    while head is not None:
        print(head.data,end="-->")
        head = head.next
    print('None')
    return

def takeInput():
    arr = list(int(ele) for ele in input().split())
    head = None
    tail = None
    for currData in arr:
        if currData == -1:
            break
        newNode = Node(currData)        
        if head is None:
            head = newNode
            tail = newNode
        else: 
            tail.next = newNode
            tail = newNode                
    return head

head = takeInput() 
head=reverse(head)
printLL(head)