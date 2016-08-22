//: Playground - noun: a place where people can play

import Foundation

// 3.1
struct ThreeStackInOne<T> {
    var arr = [T?](repeatElement(nil, count: 3))
    
    var top = [0,1,2]
    var base = [0,1,2]

    mutating func push(_ value: T, to stack: Int) {
        if arr[top[stack]] == nil {
            arr[top[stack]] = value
        } else {
            arr.insert(value, at: top[stack] + 1)

            if stack == 0 { top = top.map { $0 + 1 } ; base[1] += 1 ; base[2] += 1 }
            else if stack == 1 { top[1] += 1; top[2] += 1 ; base[2] += 1  }
            else { top[2] += 1}
        }
    }
    
    mutating func pop(from stack: Int) -> T? {
        if top[stack] == base[stack] {
            let val = arr[top[stack]]
            arr[top[stack]] = nil
            return val
        } else {
            let val = arr.remove(at: top[stack])
            top[stack] -= 1
            if stack == 0 { top[1] -= 1; top[2] -= 1; base[1] -= 1 ; base[2] -= 1 }
            else if stack == 1 { top[2] -= 1; base[2] -= 1  }
            return val
        }
    }
    
    func print(from stack: Int) -> [T?]{
        var ret = [T?]()
        for i in base[stack]...top[stack] {
            ret.append(arr[i])
        }
        return ret
    }
}

var threeStack = ThreeStackInOne<Int>()

threeStack.push(1, to: 0)
threeStack.push(2, to: 0)
threeStack.push(3, to: 0)
threeStack.push(4, to: 1)
threeStack.push(5, to: 1)
threeStack.push(6, to: 1)
threeStack.push(7, to: 2)
threeStack.push(8, to: 2)
threeStack.push(9, to: 2)
threeStack.print(from: 0)
threeStack.print(from: 1)
threeStack.print(from: 2)
threeStack.pop(from: 0)
threeStack.pop(from: 0)
threeStack.pop(from: 0)
threeStack.print(from: 0)
threeStack.top
threeStack.base
threeStack.pop(from: 1)
threeStack.pop(from: 1)
threeStack.pop(from: 1)
threeStack.pop(from: 2)
threeStack.pop(from: 2)
threeStack.pop(from: 2)


// 3.2
struct Stack<T: Comparable> {
    var arr = [T]()
    var min: T? = nil
    
    mutating func push(_ obj: T) {
        arr.append(obj)
        
        if min == nil {
            min = obj
        } else if obj < min! {
            min = obj
        }
    }
    
    mutating func pop() -> T? {
        return arr.count > 0 ? arr.removeLast() : nil
    }

}

var stack = Stack<Int>()
stack.push(1)
stack.push(2)
stack.push(3)
stack.arr
stack.min

stack.pop()
stack.pop()
stack.pop()
stack.pop()


// 3.3 

struct SetOfStacks<T> {
    var stacks = [[T]]()
    var top = 0
    var maxSize: Int
    
    init(maxSize: Int = 10) {
        self.maxSize = maxSize
    }

    mutating func push(_ obj: T) {
        if stacks.count == 0 {
            stacks.append([])
        }

        if stacks[top].count == maxSize {
            stacks.append([obj])
            top += 1
        } else {
            stacks[top].append(obj)
        }
    }

    mutating func pop() -> T? {
        if stacks.count == 0 || stacks[top].count == 0 {
            return nil
        }

        let ret = stacks[top].removeLast()
        if stacks[top].count == 0 {
            stacks.remove(at: top)
            top -= 1
        }
        return ret

    }
}
var stacks = SetOfStacks<Int>(maxSize: 1)
stacks.push(1)
stacks.stacks
stacks.push(2)
stacks.stacks
stacks.push(3)
stacks.stacks
stacks.pop()
stacks.stacks
stacks.pop()
stacks.stacks
stacks.pop()
stacks.stacks
stacks.pop()
stacks.stacks