from tkinter import *
from tkinter import ttk, messagebox
from Grocery_db import GMS

db = GMS("GMS.db")

def refresh():
    for item in tree.get_children():
        tree.delete(item)
    rows = db.fetch()
    for row in rows:
        id_val,product_name,price,qty = row
        tree.insert("","end",values=(id_val,product_name,price,qty))


def add():
    product_name = product_name_entry.get()
    price = price_entry.get()
    qty = qty_entry.get()
    id_val = len(tree.get_children()) + 1

    if product_name == "" or price == "" or qty == "":
        messagebox.showwarning("Warning","Fill All Fields")

    tree.insert("","end",values=(id_val,product_name,price,qty))
    db.add(product_name,price,qty)

    product_name_entry.delete(0,END)
    price_entry.delete(0,END)
    qty_entry.delete(0,END)

def select_item(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')

    if values:
        id_val,product_name,price,qty = values
        product_name_entry.delete(0,END)
        price_entry.delete(0,END)
        qty_entry.delete(0,END)
        
        product_name_entry.insert(0,product_name)
        price_entry.insert(0,price)
        qty_entry.insert(0,qty)

def update():
    selected = tree.focus()

    values = tree.item(selected, "values") 
    id_val = values[0]   

    product_name = product_name_entry.get()
    price = price_entry.get()
    qty = qty_entry.get()  

    db.update(id_val,product_name,price,qty)

    refresh()
    product_name_entry.delete(0,END)
    price_entry.delete(0,END)
    qty_entry.delete(0,END)

def delete():
    selected = tree.focus()

    values = tree.item(selected, "values") 
    id_val = values[0] 
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    if confirm:
        db.delete(id_val)
    else:
        messagebox.showinfo("Delete","Cancelled")
        return
    refresh()
    messagebox.showinfo("Deleted","Deleted Sucessfully")

    product_name_entry.delete(0,END)
    price_entry.delete(0,END)
    qty_entry.delete(0,END)

window = Tk()
window.geometry("1020x700")
window.title("Grocery Management System")
window.config(bg="#ffffff")

Label(window, 
      text="Grocery Management System", 
      bg="grey", 
      font=("Arial", 20, "bold"), 
      width=60).grid(row=0, column=0,columnspan=3, pady=10)


Label(window, text="Product Name", font=("Arial", 15,"bold"), width=20).grid(row=1, column=0, padx=5, pady=5)
Label(window, text="Price", font=("Arial", 15, "bold"), width=20).grid(row=1, column=1, padx=5, pady=5)
Label(window, text="Quantity", font=("Arial", 15, "bold"), width=20).grid(row=1, column=2, padx=5, pady=5)

product_name_entry = Entry(width=20, font=("Arial", 15, "bold"))
product_name_entry.grid(row=2,column=0,padx=5,pady=5)
price_entry = Entry(width=20, font=("Arial", 15, "bold"))
price_entry.grid(row=2,column=1,padx=5,pady=5)
qty_entry = Entry(width=20, font=("Arial", 15, "bold"))
qty_entry.grid(row=2,column=2,padx=5,pady=5)

Button(text="Add",width=18, font=("Arial", 15, "bold"),bg="#0077b6",command=add).grid(row=3,column=0,padx=10,pady=10)
Button(text="Update",width=18, font=("Arial", 15, "bold"),bg="#6a994e",command=update).grid(row=3,column=1,padx=10,pady=10)
Button(text="Delete",width=18, font=("Arial", 15, "bold"),bg="#bc4749",command=delete).grid(row=3,column=2,padx=10,pady=10)


tree_frame = LabelFrame(window, text="Grocery Items")
tree_frame.grid(row=5, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

column = ["ID","Name","Price","Quantity"]

tree = ttk.Treeview(tree_frame,columns=column,show="headings")

for col in column:
    tree.heading(col,text=col)
    tree.column(col,anchor=CENTER)

tree.pack(fill=BOTH,expand=True,padx=20,pady=20)
tree.bind("<<TreeviewSelect>>", select_item)
refresh()

window.mainloop() 