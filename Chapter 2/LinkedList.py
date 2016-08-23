class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
    
    def asArray(self):
        arr = []
        
        tmp = self
        while tmp != None:
            arr.append(tmp.value)
            tmp = tmp.next

        return arr

class LinkedList:

    def __init__(self,):
        self.head = None
        self.length = 0

    def append(self,value):

        newNode = Node(value)
    
        if self.head == None:
            self.head = newNode
            self.length += 1
            return

        tmp = self.head

        while tmp.next != None:
            tmp = tmp.next

        tmp.next = newNode
        self.length += 1
    
    def delete(self,value):
        
        tmp = self.head
        
        if self.head == None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            
        while tmp.next != None:
            if tmp.next.value == value:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next
    
    def removeDups(self):
        tmp = self.head
        
        mp = {tmp.value: 1}

        while tmp.next != None:
            if tmp.next.value in mp:
                tmp.next = tmp.next.next
                continue
            mp[tmp.next.value] = 1
            tmp = tmp.next

    def asArray(self):
        arr = []

        tmp = self.head

        while tmp != None:
            arr.append(tmp.value)
            tmp = tmp.next

        return arr
    
    def sort(self):
        self. head = sort(self.head,self.length)

# Merge Sort
def sort(head, size):
        if size <= 1:
            return head
        head1 = head
        head2 = None
        tmp = head
        for i in range(size//2):
            tmp = tmp.next
        head2 = tmp
        head1.next = None
        lhs = sort(head1, size//2)
        rhs = sort(head2, size - size//2)
        return merge(lhs,rhs)
        
def merge(lHead,rHead):
        head = Node(-1)
        tmp = head

        while lHead != None or rHead != None:
            if lHead == None:
                tmp.next = rHead
                rHead = rHead.next
                tmp = tmp.next
            elif rHead == None:
                tmp.next = lHead
                lHead = lHead.next
                tmp = tmp.next
            else:
                if lHead.value < rHead.value:
                    tmp.next = lHead
                    lHead = lHead.next
                    tmp = tmp.next
                else:
                    tmp.next = rHead
                    rHead = rHead.next
                    tmp = tmp.next
        return head.next 

ll = LinkedList()

ll.append(3)
ll.append(5)
ll.append(1)
ll.append(7)

print(ll.asArray())
ll.sort()
print(ll.asArray())
ll.delete(3)
print(ll.asArray())
