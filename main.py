import tkinter as tk
from tkinter import messagebox
from inventory_bst import InventoryBST
from order_queue import OrderQueue

inventory = InventoryBST()
orders = OrderQueue()

# ---------------- FUNCTIONS ----------------

def add_product():
    try:
        inventory.insert(
            int(pid_entry.get()),
            name_entry.get(),
            int(qty_entry.get()),
            float(price_entry.get())
        )
        messagebox.showinfo("Success", "Product added successfully")
    except:
        messagebox.showerror("Error", "Invalid input")

def search_product():
    try:
        product = inventory.search(int(search_entry.get()))
        if product:
            messagebox.showinfo(
                "Product Found",
                f"Name: {product.name}\nQuantity: {product.qty}\nPrice: {product.price}"
            )
        else:
            messagebox.showerror("Error", "Product not found")
    except:
        messagebox.showerror("Error", "Invalid Product ID")

def delete_product():
    try:
        pid = int(delete_entry.get())

        if inventory.delete(pid):
            messagebox.showinfo("Success", "Product deleted successfully")
            display_inventory()
        else:
            messagebox.showerror("Error", "Invalid Product ID")

    except ValueError:
        messagebox.showerror("Error", "Enter valid Product ID")


def place_order():
    try:
        orders.add_order(int(order_pid.get()), int(order_qty.get()))
        messagebox.showinfo("Success", "Order placed successfully")
    except:
        messagebox.showerror("Error", "Invalid order input")

def process_order():
    result = orders.process_order(inventory)
    messagebox.showinfo("Order Status", result)

def display_inventory():
    display_box.delete(1.0, tk.END)
    display_box.insert(tk.END, "ID\tName\tQty\tPrice\n")
    display_box.insert(tk.END, "-" * 40 + "\n")
    for p in inventory.inorder():
        display_box.insert(tk.END, f"{p.pid}\t{p.name}\t{p.qty}\t{p.price}\n")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Inventory Management System (DSA)")
root.geometry("500x800")

# ADD PRODUCT
tk.Label(root, text="Add Product", font=("Arial", 14)).pack(pady=5)
pid_entry = tk.Entry(root)
pid_entry.insert(0, "Product ID")
pid_entry.pack()
name_entry = tk.Entry(root)
name_entry.insert(0, "Product Name")
name_entry.pack()
qty_entry = tk.Entry(root)
qty_entry.insert(0, "Quantity")
qty_entry.pack()
price_entry = tk.Entry(root)
price_entry.insert(0, "Price")
price_entry.pack()
tk.Button(root, text="Add Product", command=add_product).pack(pady=5)

# SEARCH PRODUCT
tk.Label(root, text="Search Product", font=("Arial", 14)).pack(pady=10)
search_entry = tk.Entry(root)
search_entry.insert(0, "Product ID")
search_entry.pack()
tk.Button(root, text="Search", command=search_product).pack(pady=5)

# DELETE PRODUCT
tk.Label(root, text="Delete Product", font=("Arial", 14)).pack(pady=10)
delete_entry = tk.Entry(root)
delete_entry.insert(0, "Product ID")
delete_entry.pack()
tk.Button(root, text="Delete Product", command=delete_product).pack(pady=5)

# ORDER SECTION
tk.Label(root, text="Order Section", font=("Arial", 14)).pack(pady=10)
order_pid = tk.Entry(root)
order_pid.insert(0, "Product ID")
order_pid.pack()
order_qty = tk.Entry(root)
order_qty.insert(0, "Quantity")
order_qty.pack()
tk.Button(root, text="Place Order", command=place_order).pack(pady=5)
tk.Button(root, text="Process Order", command=process_order).pack(pady=5)

# DISPLAY INVENTORY
tk.Button(root, text="Display Inventory", command=display_inventory).pack(pady=10)
display_box = tk.Text(root, height=10)
display_box.pack()

root.mainloop()
