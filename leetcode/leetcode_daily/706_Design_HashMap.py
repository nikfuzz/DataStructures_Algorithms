'''
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output
[null, null, null, 1, -1, null, 1, null, -1]

Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove
'''

class HashNode:
    def __init__(self, key=-1, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_map = [None]*self.size
        

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        prev = curr_node = self.hash_map[hash_key]
        
        if not curr_node:
            self.hash_map[hash_key] = HashNode(key, value)
            return
            
        else:
            while curr_node:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                
                prev = curr_node
                curr_node = curr_node.next
                
            prev.next = HashNode(key, value)
                
        return
        
        

    def get(self, key: int) -> int:
        hash_key = key % self.size
        curr_node = self.hash_map[hash_key]
        
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            
            curr_node = curr_node.next
        
        return -1
        

    def remove(self, key: int) -> None:
        hash_key = key % self.size
        prev = curr_node = self.hash_map[hash_key]
        
        if curr_node and curr_node.key == key:
            self.hash_map[hash_key] = curr_node.next
            return
        
        while curr_node:
            if curr_node.key == key:
                prev.next = curr_node.next
                return
            prev, curr_node = curr_node, curr_node.next
            
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# time O(N)
# space O(N)