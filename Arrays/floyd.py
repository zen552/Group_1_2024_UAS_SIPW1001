class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt
    def __repr__(self):
        return f"Node({self.val})"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

class Floyd:
    def run(*params):
        if isinstance(params[0], LinkedList):
            return Floyd.cycle(params[0])
        elif isinstance(params[0], list):
            return Floyd.find_duplicate(params[0])

    def cycle(llist):
        slow = llist.head
        fast = llist.head
        met = False
        while fast and fast.nxt:
            slow = slow.nxt
            fast = fast.nxt.nxt
            if slow == fast:
                met = True
                break
        if not met:
            return None
        slow = llist.head
        while slow != fast:
            slow = slow.nxt
            fast = fast.nxt
        return slow

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
if __name__ == "__main__":
    # Membuat linked list dengan siklus
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4
    node4.nxt = node2  # Siklus di sini

    ll = LinkedList(node1)
    result = Floyd.cycle(ll)
    if result:
        print(f"Siklus ditemukan di node dengan nilai: {result.val}")
    else:
        print("Tidak ada siklus.")