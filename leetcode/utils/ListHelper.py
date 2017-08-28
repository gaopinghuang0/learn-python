
# A helper script related to singly-linked list.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def array_to_list(arr):
    """convert a list of values to a linked list"""
    if not arr:
        return None

    node = ListNode(arr[0])
    head = node
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        node.next = new_node
        node = new_node
    return head

def linked_list_to_array(node):
    if not node:
        return []

    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def print_linked_list(node):
    if not node:
        return False

    while True:
        print(node.val,)
        node = node.next
        if node:
            print('->',)
        else:
            break
    print('\n')


def main():
    linked_list = array_to_list([1,2,3])
    print_list(linked_list)


if __name__ == '__main__':
    main()
