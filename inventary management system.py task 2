import tkinter as tk
from tkinter import ttk, messagebox

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        self.inventory = {}

        # Main Frame to center content
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(expand=True)

        # UI Elements
        ttk.Label(self.main_frame, text="Item Name:").grid(row=0, column=0, padx=10, pady=5)
        self.item_entry = ttk.Entry(self.main_frame)
        self.item_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.main_frame, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        self.qty_entry = ttk.Entry(self.main_frame)
        self.qty_entry.grid(row=1, column=1, padx=10, pady=5)

        self.check_var = tk.IntVar()
        self.check_button = ttk.Checkbutton(self.main_frame, text="Mark as Essential", variable=self.check_var)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=5)

        ttk.Button(self.main_frame, text="Add Item", command=self.add_item).grid(row=3, column=0, pady=10)
        ttk.Button(self.main_frame, text="Clear Fields", command=self.clear_fields).grid(row=3, column=1, pady=10)
        ttk.Button(self.main_frame, text="Reset Inventory", command=self.reset_inventory).grid(row=3, column=2, pady=10)
        
        # Center the table
        self.tree_frame = ttk.Frame(self.main_frame)
        self.tree_frame.grid(row=4, column=0, columnspan=3, pady=20, padx=50)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Item", "Quantity", "Essential"), show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Essential", text="Essential")
        self.tree.pack(expand=True, fill="both")

        ttk.Button(self.main_frame, text="Remove Item", command=self.remove_item).grid(row=5, column=0, pady=10)
        ttk.Button(self.main_frame, text="Update Item", command=self.update_item).grid(row=5, column=1, pady=10)
        ttk.Button(self.main_frame, text="Show Inventory", command=self.show_inventory).grid(row=5, column=2, pady=10)
        ttk.Button(self.main_frame, text="Exit", command=root.quit).grid(row=6, column=1, pady=10)

    def add_item(self):
        item = self.item_entry.get().strip()
        qty = self.qty_entry.get().strip()
        essential = "Yes" if self.check_var.get() else "No"

        if item and qty.isdigit():
            qty = int(qty)
            self.inventory[item] = (qty, essential)
            self.update_tree()
        else:
            messagebox.showerror("Error", "Invalid input")

    def remove_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item, "values")[0]
            del self.inventory[item]
            self.update_tree()
        else:
            messagebox.showwarning("Warning", "No item selected")

    def update_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item, "values")[0]
            new_qty = self.qty_entry.get().strip()
            essential = "Yes" if self.check_var.get() else "No"
            if new_qty.isdigit():
                self.inventory[item] = (int(new_qty), essential)
                self.update_tree()
            else:
                messagebox.showerror("Error", "Invalid quantity")
        else:
            messagebox.showwarning("Warning", "No item selected")
    
    def clear_fields(self):
        self.item_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.check_var.set(0)
    
    def reset_inventory(self):
        self.inventory.clear()
        self.update_tree()
        messagebox.showinfo("Reset", "Inventory has been reset")

    def show_inventory(self):
        inventory_list = "\n".join([f"{item}: {qty} ({essential})" for item, (qty, essential) in self.inventory.items()])
        messagebox.showinfo("Inventory", inventory_list if inventory_list else "No items in inventory")
    
    def update_tree(self):
        self.tree.delete(*self.tree.get_children())
        for item, (qty, essential) in self.inventory.items():
            self.tree.insert("", "end", values=(item, qty, essential))

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
