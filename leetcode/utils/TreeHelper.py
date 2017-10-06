# TreeHelper.py
# A helper script related to tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_tree(arr):
    """convert a list of values to a tree"""
    if not arr:
        return None
    if arr[0] is None:
        if len(arr) > 1:
            raise Exception('root must not be None')
        else:
            return []

    root = TreeNode(arr[0])
    nodes = [root]
    n = len(arr)
    for i in range(n//2+1):
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and arr[left] is not None:
            leftNode = TreeNode(arr[left])
        else:
            leftNode = None
        if nodes[i] is None:
            if leftNode is not None:
                raise Exception
        else:
            nodes[i].left = leftNode
        nodes.append(leftNode)

        if right < n and arr[right] is not None:
            rightNode = TreeNode(arr[right])
        else:
            rightNode = None
        if nodes[i] is None:
            if rightNode is not None:
                raise Exception
        else:
            nodes[i].right = rightNode
        nodes.append(rightNode)

    return root

def array_to_BST(arr):
    """Binary search tree."""
    if not arr:
        return None
    root = TreeNode(arr[0])
    for x in arr[1:]:
        node = root
        while True:
            if x < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(x)
                    break
            elif x > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(x)
                    break
            else:
                break

    return root

def search_in_BST(root, val):
    p = root
    while p:
      if val < p.val:
        p = p.left
      elif val > p.val:
        p = p.right
      else:
        break
    return p

# Naive way
def print_in_level_order(root, empty="None"):
    stack = [root]
    temp = []
    while len(stack):
        node = stack.pop(0)
        if node is not None:
            print(node.val, ' ', end='')
            temp.append(node.left)
            temp.append(node.right)
        else:
            print(empty, ' ', end='')
            temp.append(None)
            temp.append(None)
        if len(stack) == 0:
            print()
            if len(list(filter(lambda x: x is not None, temp))) == 0:
                break   # break when all nodes are None
            stack = temp[:]
            temp = []

if __name__ == "__main__":
    def main():
        root = array_to_tree([1, 2, 3, 4, None, 5, None, None, 6])
        # print root.val, root.left.val
        print_in_level_order(root)

    main()