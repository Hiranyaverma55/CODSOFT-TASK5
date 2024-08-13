import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Info", "Contact added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name is required.")

def view_contacts():
    contacts_list.delete(1.0, tk.END)
    if contacts:
        for name, details in contacts.items():
            contacts_list.insert(tk.END, f"Name: {name}, Phone: {details['phone']}\n")
    else:
        contacts_list.insert(tk.END, "No contacts found.")

def search_contact():
    query = search_entry.get()
    results = {name: details for name, details in contacts.items() if query in name or query in details['phone']}
    contacts_list.delete(1.0, tk.END)
    if results:
        for name, details in results.items():
            contacts_list.insert(tk.END, f"Name: {name}, Phone: {details['phone']}\n")
    else:
        contacts_list.insert(tk.END, "No contacts found.")

def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name in contacts:
        if phone: contacts[name]['phone'] = phone
        if email: contacts[name]['email'] = email
        if address: contacts[name]['address'] = address
        messagebox.showinfo("Information", "Contact updated successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Information", "Contact deleted successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Contact not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Contact Book")

tk.Label(app, text="Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Phone:").pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

tk.Label(app, text="Email:").pack()
email_entry = tk.Entry(app)
email_entry.pack()

tk.Label(app, text="Address:").pack()
address_entry = tk.Entry(app)
address_entry.pack()

tk.Label(app, text="Search:").pack()
search_entry = tk.Entry(app)
search_entry.pack()
tk.Label(app, text="Delete:").pack()
delete_entry = tk.Entry(app)
delete_entry.pack()

tk.Button(app, text="Search Contact", command=search_contact).pack()
tk.Button(app, text="Add Contact", command=add_contact).pack()
tk.Button(app, text="Update Contact", command=update_contact).pack()
tk.Button(app, text="View Contacts", command=view_contacts).pack()
tk.Button(app, text="Delete Contact", command=delete_contact).pack()

contacts_list = tk.Text(app, height=20, width=70)
contacts_list.pack()

app.mainloop()
