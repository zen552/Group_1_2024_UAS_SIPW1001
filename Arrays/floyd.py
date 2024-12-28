class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt
    def __repr__(self):
        return f"Node({self.val})"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def cycle(llist):
    ptr = llist.head
    visited = set()
    while ptr is not None:
        if ptr in visited:
            return ptr
        else:
            visited.add(ptr)
            ptr = ptr.nxt
    return None

def cycle(llist):
    slow = llist.head
    fast = llist.head
    met = False
    while fast is not None and fast.nxt is not None:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            met = True
            break
    if not met:
        return None
    else:
        slow = llist.head
        while slow != fast:
            slow = slow.nxt
            fast = fast.nxt
    return slow

def find_duplicate(arr):
    visited = set()
    for elem in arr:
        if elem in visited:
            return elem
        else:
            visited.add(elem)

def find_duplicate(arr):
    slow = 0
    fast = 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

#Contoh Penggunaan Floyd's Algorithm
# Membuat Linked List dengan siklus
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.nxt = node2
node2.nxt = node3
node3.nxt = node4
node4.nxt = node2

ll = LinkedList(node1)
print(cycle(ll))