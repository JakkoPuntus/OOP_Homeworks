#Лучшее из того, что выходило. Для поиска используется дерево отрезков, дополненное балансировкой по типу авл дерева
#15 тестов на python 3.8 проходит, 14 на pypy


class Node:
    def __init__(self, s=None, e=None):
        self.start = s
        self.end = e
        self.val = e-s+1
        self.left = None
        self.right = None
        self.destroyed_rooms = 0
        self.height = 1

    def update(self, s, e):
        self.start = s
        self.end = e
        self.val = e-s+1

def right_rotate(a: Node) -> Node:
    b = a.left
    t = b.right

    b.right = a
    a.left = t

    a.height = max(a.left.height, a.right.height) + 1
    b.height = max(b.left.height, b.right.height) + 1

    a.destroyed_rooms = a.left.destroyed_rooms + a.right.destroyed_rooms + 1
    b.destroyed_rooms = b.left.destroyed_rooms + b.right.destroyed_rooms + 1

    a.update(a.left.start, a.right.end)
    b.update(b.left.start, b.right.end)

    return b


def left_rotate(a: Node) -> Node:
    b = a.right
    t = b.left

    b.left = a
    a.right = t

    a.height = max(a.left.height, a.right.height) + 1
    b.height = max(b.left.height, b.right.height) + 1

    a.destroyed_rooms = a.left.destroyed_rooms + a.right.destroyed_rooms + 1
    b.destroyed_rooms = b.left.destroyed_rooms + b.right.destroyed_rooms + 1

    a.update(a.left.start, a.right.end)
    b.update(b.left.start, b.right.end)

    return b


def get_balance(N: Node) -> int:
    if N is None:
        return 0
    return N.left.height - N.right.height


def search(root: Node, r: int) -> int:
    if root.left is None and root.right is None:
        return root.start + r - 1

    else:
        lNode = root.left
        left_rooms = lNode.val - lNode.destroyed_rooms

        if left_rooms >= r:
            return search(root.left, r)
        else:
            return search(root.right, r-left_rooms)


def split(root: Node, r: int) -> Node:
    root.destroyed_rooms += 1

    if root.left is None and root.right is None:
        split_point = root.start + r - 1

        root.left = Node(root.start, split_point - 1)
        root.right = Node(split_point + 1, root.end)
        root.height += 1

    else:
        lNode = root.left
        left_rooms = lNode.val - lNode.destroyed_rooms

        if left_rooms >= r:
            root.left = split(root.left, r)
        else:
            root.right = split(root.right, r - left_rooms)

        root.height = 1 + max(root.left.height, root.right.height)

        balance = get_balance(root)

        if balance < -1:
            lc = root.right.left
            rc = root.right.right

            if lc.height > rc.height:
                root.right = right_rotate(root.right)
                return left_rotate(root)
            else:
                return left_rotate(root)
            
        if balance > 1:
            lc = root.left.left
            rc = root.left.right

            if lc.height > rc.height:
                return right_rotate(root)
            else:
                root.left = left_rotate(root.left)
                return right_rotate(root)
            
    return root


N, M = map(int, input().split())

root = Node(1, N)

while M:
    c, n = input().split()
    n = int(n)

    if c == 'L':
        print(search(root, n))
    else:
        root = split(root, n)
    M -= 1