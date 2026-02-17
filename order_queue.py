class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, pid, qty):
        self.queue.append((pid, qty))

    def process_order(self, inventory):
        if not self.queue:
            return "No pending orders"

        pid, qty = self.queue.pop(0)
        product = inventory.search(pid)

        if product and product.qty >= qty:
            product.qty -= qty
            return f"Order processed for Product ID {pid}"
        else:
            return "Order failed (Product not found or insufficient stock)"
