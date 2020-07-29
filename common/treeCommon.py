from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def genTree(arr: List[int]):
    if len(arr) == 0:
        return None
    root = addNode(0, arr)
    return root

def test_tree():
    return genTree([1,2,3,4,5,6,7])

def addNode(i, arr):
    node = TreeNode(arr[i])
    if i * 2 + 1 < len(arr) and arr[i * 2 + 1] is not None:
        node.left = addNode(i * 2 + 1, arr)
    else:
        node.left = None

    if i * 2 + 2 < len(arr) and arr[i * 2 + 2] is not None:
        node.right = addNode(i * 2 + 2, arr)
    else:
        node.right = None

    return node



