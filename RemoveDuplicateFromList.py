class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


def removeDuplicates(head):
    previous = None
    current = head
    s = set()
    while current:
        if current.data in s:
            previous.next = current.next
        else:
            s.add(current.data)
            previous = current
        current = previous.next
    return head


def keepUnique(head):
    p, f, c = None, False, head

    while c:
        if (c.next and c.data == c.next.data) or f == True:
            f = True if c.data == c.next.data else False
            if p != None:
                p.next = c.next
            else:
                head = c.next
            t = c
            c = c.next
            del t
        else:
            p = c
            c = c.next
    return head


if __name__ == '__main__':
    #keys = [5, 3, 4, 2, 5, 4, 1, 3]
    #keys = [1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9]
    keys = [3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9]
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    # removeDuplicates(head)
    head = keepUnique(head)
    printList(head)
