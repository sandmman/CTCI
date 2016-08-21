
extension String {
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
}



"test".isUnique
"tes".isUnique
"2".isUnique2
"".isUnique

"test".isUnique2
"tes".isUnique2
"1".isUnique2
"".isUnique2
