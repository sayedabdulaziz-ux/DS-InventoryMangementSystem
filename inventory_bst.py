class ProductNode:
    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price
        self.left = None
        self.right = None


class InventoryBST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, pid, name, qty, price):
        self.root = self._insert(self.root, pid, name, qty, price)

    def _insert(self, node, pid, name, qty, price):
        if node is None:
            return ProductNode(pid, name, qty, price)
        if pid < node.pid:
            node.left = self._insert(node.left, pid, name, qty, price)
        elif pid > node.pid:
            node.right = self._insert(node.right, pid, name, qty, price)
        return node

    # SEARCH
    def search(self, pid):
        return self._search(self.root, pid)

    def _search(self, node, pid):
        if node is None or node.pid == pid:
            return node
        if pid < node.pid:
            return self._search(node.left, pid)
        return self._search(node.right, pid)

    # INORDER DISPLAY
    def inorder(self):
        products = []
        self._inorder(self.root, products)
        return products

    def _inorder(self, node, products):
        if node:
            self._inorder(node.left, products)
            products.append(node)
            self._inorder(node.right, products)

    # ✅ DELETE (FIXED)
    def delete(self, pid):
        self.root, deleted = self._delete(self.root, pid)
        return deleted

    def _delete(self, node, pid):
        if node is None:
            return node, False

        if pid < node.pid:
            node.left, deleted = self._delete(node.left, pid)

        elif pid > node.pid:
            node.right, deleted = self._delete(node.right, pid)

        else:
            # Node found
            if node.left is None and node.right is None:
                return None, True

            if node.left is None:
                return node.right, True

            if node.right is None:
                return node.left, True

            # Two children
            temp = self._min_value_node(node.right)
            node.pid = temp.pid
            node.name = temp.name
            node.qty = temp.qty
            node.price = temp.price
            node.right, _ = self._delete(node.right, temp.pid)
            return node, True

        return node, deleted

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
