//: Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"


class Node<T: Hashable> {
    var value: T
    var next: Node? = nil
    var prev: Node? = nil
    
    init(_ value: T) {
        self.value = value
    }
}

public class LinkedList<T: Hashable> {
    var head: Node<T>? = nil
    var tail: Node<T>? = nil
    var length: Int = 0
    
    public func append(_ value: T) {
        let newNode = Node<T>(value)
        if var tmp = head {
            while let next = tmp.next {
                tmp = next
            }
            newNode.prev = tmp
            tmp.next = newNode
            tail = newNode
        } else {
            head = newNode
            tail = newNode
        }
        length += 1
    }
    
    public func delete(_ value: T) {
        if var tmp = head {
            // Value is our head
            if tmp.value == value {
                head = tmp.next
                length -= 1
                return
            }
            while let next = tmp.next {
                if next.value == value {
                    tmp.next = next.next
                    length -= 1
                    return
                }
                tmp = next
            }
        }
    }
    
    // 2.1.1
    public func removeDups() {
        var map = [T:Bool]()
        
        if var tmp = head {
            map[tmp.value] = true
            while let next = tmp.next {
                if map[next.value] != nil {
                    tmp.next = next.next
                    length -= 1
                } else {
                    map[next.value] = true
                    tmp = next
                }
            }
        }
    }

    // 2.1.2 without buffer
    public func removeDups2() {
        //head = sorted(head)
        
        if var tmp = head {
            while let next = tmp.next {
                if tmp.value == next.value {
                    tmp.next = next.next
                    length -= 1
                } else {
                    tmp = next
                }
            }
        }
    }

    // 2.2
    public func nthToLast(_ nth: Int) -> T? {
        var n = nth - 1

        if var ptr1 = head, var ptr2 = head {
            while let next = ptr2.next, n != 0 {
                ptr2 = next
                n -= 1
            }
            
            if n != 0 { return nil }
            
            while let nxt = ptr2.next {
                ptr2 = nxt
                ptr1 = ptr1.next!
            }
            
            return ptr1.value
        }

        return nil
    }
    var asArray: [T]  {
        var arr = [T]()
        var tmp = head
        
        while tmp != nil{
            arr.append(tmp!.value)
            tmp = tmp!.next
        }
        return arr
    }
}

var list = LinkedList<String>()
list.append("1")
list.append("2")
list.append("2")
list.append("2")
list.append("3")
list.removeDups2()
list.asArray
list.append("3")
list.append("3")
list.append("2")
list.append("3")
list.asArray
list.delete("3")
list.asArray
list.removeDups()
list.asArray
list.nthToLast(1)
list.nthToLast(3)
list.nthToLast(2)