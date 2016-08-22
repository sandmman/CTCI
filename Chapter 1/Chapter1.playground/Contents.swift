//
//  Chapter 1
//
//
//  Created by Aaron Liberatore on 5/20/16.
//
//

import Foundation

extension String {

    // 1.1.1
    public var isUnique: Bool {
        var map = [Character: Int]()
        
        for ch in self.characters {
            if map[ch] != nil {
                return false
            } else {
                map[ch] = 1
            }
        }
        return true
    }

    // 1.1.2
    public var isUnique2: Bool {
        let tmp = self.characters.sorted()
        
        if tmp.count <= 1 { return true }
        
        for i in 0..<tmp.count - 1 {
            if tmp[i] == tmp[i+1] {
                return false
            }
        }
        return true
    }

    // 1.2
    var reversed: String {
        return self.characters.reversed().map { String($0)}.joined(separator: "")
    }

    // 1.2
    var reversed2: String {
        var str = ""
        var tmp = characters
        for _ in (0..<characters.count) {
            str += String(tmp[tmp.index(before: tmp.endIndex)])
            tmp = tmp.dropLast(1)
        }
        return str
    }

    // 1.3
    var removeDups: String {
        mutating get {
            //var map = [Character: Int]()
            //var index = characters.count
            /*for i in 0..<index {
             if map[characters.startIndex.] == nil {
             map[characters[i]] = 0
             }
             map[characters[i]] += 1
             self.remove(at: self.index(startIndex, offsetBy: i))
             index -= 1
             }*/
            return self
        }
    }
    
    // 1.4
    func isAnagram(of str: String) -> Bool {
        var map = [Character: Int]()
        
        for char in self.characters {
            if map[char] != nil {
                map[char]! += 1
            }
            map[char] = 1
        }

        for char in str.characters {
            if map[char] == nil {
                return false
            } else {
                map[char]! -= 1
                if map[char]! < 0 {
                    return false
                }
            }
        }
        return true
    }
    // 1.5
    var replaceSpaces: String {
        return self.replacingOccurrences(of: " ", with: "%20")
    }

    // 1.8
    func isSubstring(of str: String) -> Bool {
        return self.magicIsSubstring(of: "\(str)\(str)")
        
    
    }
    // Magic function given in 1.8
    func magicIsSubstring(of str: String) -> Bool {
        return true
    }
}

// 1.6
func rotate(_ table: [[Int]]) -> [[Int]] {
    var table = table
    (table.count / 2 ) + 1
    for layer in 0..<(table.count / 2 ){
        
        // Exchange corners
        let c1 = table[layer][layer]
        let c2 = table[layer][table.count - 1 - layer]
        let c3 = table[table.count - 1 - layer][table.count - 1 - layer]
        let c4 = table[table.count - 1 - layer][layer]
        
        table[layer][layer] = c4
        table[layer][table.count - 1 - layer] = c1
        table[table.count - 1 - layer][table.count - 1 - layer] = c2
        table[table.count - 1 - layer][layer] = c3

        if layer != table.count / 2 - 1 {
            for i in (layer + 1)..<((table.count / 2 ) + 1 ) {

                    let c1 = table[layer][i]
                    let c2 = table[i][table.count - 1 - layer]
                    let c3 = table[table.count - 1 - layer][table.count - 1 - i]
                    let c4 = table[table.count - 1 - i][layer]
                    
                        c1
                     c2
                     c3
                     c4
                     
                    table[layer][i] = c4
                    table[i][table.count - 1 - layer] = c1
                    table[table.count - 1 - layer][table.count - 1 - i] = c2
                    table[table.count - 1 - i][layer] = c3
                }
        }
    }
    return table
}
 
// 1.7

func zerofy(matrix: [[Int]]) -> [[Int]] {
    var matrix = matrix
    var rows = [Int:Int]()
    var cols = [Int:Int]()
    for i in 0..<matrix.count {
        for j in 0..<matrix[0].count {
            if matrix[i][j] == 0 {
                rows[i] = 0
                cols[j] = 0
            }
        }
    }

    for i in 0..<matrix.count {
        for j in 0..<matrix[0].count {
            if rows[i] != nil || cols[j] != nil {
                matrix[i][j] = 0
            }
        }
    }

    return matrix
}

// Test Cases

// 1.1
"".isUnique
"a".isUnique
"ab".isUnique
"abc".isUnique
"ABcd1".isUnique

"".isUnique2
"a".isUnique2
"ab".isUnique2
"abc".isUnique2
"ABcd1".isUnique2

// 1.2
"".reversed
"a".reversed
"ab".reversed
"abc".reversed
"ABcd1".reversed

"".reversed2
"a".reversed2
"ab".reversed2
"abc".reversed2
"ABcd1".reversed2

// 1.3
var t0 = ""
var t1 = "a"
var t2 = "aa"
var t3 = "abfgdscs"
t0.removeDups
t1.removeDups
t2.removeDups
t3.removeDups

// 1.4
"".isAnagram(of: "")
"".isAnagram(of: "abc")
"abc".isAnagram(of: "bca")
"abc".isAnagram(of: "bcca")


// 1.5
"I ran to the store".replaceSpaces

// 1.6
rotate([ [1,  2, 3,  4],
         [5,  6, 7,  8],
         [9, 10,11, 12],
         [13,14,15, 16]])

rotate([ [1,2,3],
         [4,5,6],
         [7,8,9]])

rotate([ [1,2],
         [3,4]])

// 1.7

let zeroed1 = zerofy(matrix: [])
let zeroed2 = zerofy(matrix: [[0,1],[2,2]])
let zeroed3 = zerofy(matrix: [[0,1,0],[2,2,3],[1,5,6]])

//1.8
"racecar".isSubstring(of: "acecarr")
