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
    # 2.1.1 
    def removeDups(self):
        tmp = self.head
        
        mp = {tmp.value: 1}

        while tmp.next != None:
            if tmp.next.value in mp:
                tmp.next = tmp.next.next
                continue
            mp[tmp.next.value] = 1
            tmp = tmp.next
    
    # 2.1.1 
    def removeDups1(self):
        pass

    def removeDups2(self):
        tmp = self.head
        
        mp = {tmp.value: 1}

        while tmp.next != None:
            if tmp.next.value in mp:
                tmp.next = tmp.next.next
                continue
            mp[tmp.next.value] = 1
            tmp = tmp.next

    # 2.2.1 Using Self.Length
    def nthToLast(self, n):
        tmp = self.head

        if self.length - n < 0:
            raise Exception("Not Enough Items")

        for i in range(self.length - n):
            if tmp == None:
                raise Exception("This shouldn't happen!? why are we missing elements")
            tmp = tmp.next

        return tmp.value

    # 2.2.1 Without using self.length
    ## Assumes 1st to last == arr[len(arr) -1], 2nd to last == arr[len(arr) - 2] 
    def nthToLast2(self, n):
        head1 = self.head
        head2 = self.head

        for i in range(n - 1):
            if head2.next == None:
                raise Exception("Not Enough Items")
            head2 = head2.next

        while head2.next != None:
            head1 = head1.next
            head2 = head2.next

        return head1.value

    # 2.3
    def deleteNode(self, node):
        if node == None or node.next == None:
            raise Exception("Can't be deleted")
        tmp = node.next
        node.value = tmp.value
        node.next = tmp.next
    
    # 2.4
    def addLL(self, LL):
        if self.head == None:
            return LL
        if LL.head == None:
            return self

        head = Node((self.head.value + LL.head.value) % 10)
        tmp = head
        
        carry = (self.head.value + LL.head.value) // 10

        lHead = self.head.next
        rHead = LL.head.next

        while lHead != None and rHead != None:
            if lHead == None:
                tmp.next = rHead
                break
            if rHead == None:
                tmp.next = lHead
                break
            sm = lHead.value + rHead.value + carry
            if sm >= 10:
                carry = 1
                tmp.next = Node(sm - 10)
            else:
                carry = 0
                tmp.next = Node(sm)
            lHead = lHead.next
            rHead = rHead.next
            tmp = tmp.next
        if carry == 1:
            tmp.next = Node(1)

        self.head = head

    #2.5
    def isCircular(self):
        if self.head == None:
            raise Exception("Not a circular list")

        rabbit = self.head
        hare = self.head

        while hare != None:
            rabbit = rabbit.next
            hare = hare.next.next
            if rabbit is hare:
                break

        if hare == None:
            raise Exception("Not a circular list")

        rabbit = self.head
        while rabbit is not hare:
            rabbit = rabbit.next
            hare = hare.next

        return rabbit.value

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


class Tests:

    def execute(self):
        self.testRemoveDups()
        self.testNthToLast()
        self.testDeleteNode()
        self.testSum()
        self.testIsCircular()
        
    # 2.1
    def testRemoveDups(self):
        tests = [[5],[5,5],[1,5,6,7,6,7]]
        solut = [[5],[5],[1,5,6,7]]
        
        
        for i in range(len(tests)):
            ll = LinkedList()
            for val in tests[i]:
                ll.append(val)
            ll.removeDups2()
            assert(ll.asArray() == solut[i])

        print("Passed Remvove Dups")
    # 2.2
    def testNthToLast(self):
        tests = [[],[1,5,6,7,6,7]]

        for i in range(len(tests)):
            ll = LinkedList()
            for val in tests[i]:
                ll.append(val)
            
            for k in range(2):
                if k == 0:
                    for j in range(1, len(tests[i])):
                        assert(tests[i][len(tests[i]) - j] == ll.nthToLast2(j))
                else:
                     for j in range(1, len(tests[i])):
                        assert(tests[i][len(tests[i]) - j] == ll.nthToLast(j))

        print("Passed Nth To Last")

    #2.3
    def testDeleteNode(self):
        
        nodes = [Node("a"), Node("b"), Node("c"), Node("d"), Node("e"), Node("f")]
        
        ll = LinkedList()
        ll.head = nodes[0]
        nodes[0].next = nodes[1]
        nodes[1].next = nodes[2]
        nodes[2].next = nodes[3]
        nodes[3].next = nodes[4]
        nodes[4].next = nodes[5]

            
        ll.deleteNode(nodes[2])
        assert(ll.asArray() == ["a","b","d","e","f"])

        print("Passed Delete Node")

    # 2.4 
    def testSum(self):
        tests = [([1,1,1],[2,2,2], [3,3,3]),([9,6,7],[2,3,2], [1,0,0,1])]
        for case in tests:
            ll1 = LinkedList()
            ll2 = LinkedList()
            for i in range(len(case[0])):
                ll1.append(case[0][i])
                ll2.append(case[1][i])

            ll1.addLL(ll2)

            assert(ll1.asArray() == case[2])

        print("Passed Test Sum")

    # 2.5
    def testIsCircular(self):
        ll = LinkedList()
        nodes = [Node("a"), Node("b"), Node("c"), Node("d"), Node("e"), Node("f")]
        ll.head = nodes[0]
        nodes[0].next = nodes[1]
        nodes[1].next = nodes[2]
        nodes[2].next = nodes[3]
        nodes[3].next = nodes[4]
        nodes[4].next = nodes[5]
        for i in range(len(nodes)):
            nodes[5].next = nodes[i]
            assert(ll.isCircular() == nodes[i].value)

        print("Passed isCircular")


t = Tests()
t.execute()

