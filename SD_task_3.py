import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    
    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return

    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts()
    refresh_contacts()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_fields()

# View contacts
def refresh_contacts():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

# Display selected contact details
def display_contact_details(event):
    selected = listbox_contacts.curselection()
    if selected:
        name = listbox_contacts.get(selected)
        contact = contacts[name]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact["Phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact["Email"])

# Edit an existing contact
def edit_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "No contact selected!")
        return

    old_name = listbox_contacts.get(selected)
    new_name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if not new_name or not phone or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    if old_name != new_name and new_name in contacts:
        messagebox.showerror("Error", "Contact name already exists!")
        return

    del contacts[old_name]
    contacts[new_name] = {"Phone": phone, "Email": email}
    save_contacts()
    refresh_contacts()
    messagebox.showinfo("Success", f"Contact '{old_name}' updated to '{new_name}'!")
    clear_fields()

# Delete a contact
def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showerror("Error", "No contact selected!")
        return

    name = listbox_contacts.get(selected)
    if messagebox.askyesno("Confirm", f"Are you sure you want to delete '{name}'?"):
        del contacts[name]
        save_contacts()
        refresh_contacts()
        messagebox.showinfo("Success", f"Contact '{name}' deleted!")
        clear_fields()

# Clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Manager")

contacts = load_contacts()

frame_inputs = ttk.Frame(root, padding=10)
frame_inputs.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(frame_inputs, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = ttk.Entry(frame_inputs, width=30)
entry_name.grid(row=0, column=1, padx=5)

ttk.Label(frame_inputs, text="Phone:").grid(row=1, column=0, sticky="w")
entry_phone = ttk.Entry(frame_inputs, width=30)
entry_phone.grid(row=1, column=1, padx=5)

ttk.Label(frame_inputs, text="Email:").grid(row=2, column=0, sticky="w")
entry_email = ttk.Entry(frame_inputs, width=30)
entry_email.grid(row=2, column=1, padx=5)

frame_buttons = ttk.Frame(root, padding=10)
frame_buttons.grid(row=1, column=0, columnspan=2)

ttk.Button(frame_buttons, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=5)
ttk.Button(frame_buttons, text="Edit Contact", command=edit_contact).grid(row=0, column=1, padx=5)
ttk.Button(frame_buttons, text="Delete Contact", command=delete_contact).grid(row=0, column=2, padx=5)
ttk.Button(frame_buttons, text="Clear Fields", command=clear_fields).grid(row=0, column=3, padx=5)

frame_list = ttk.Frame(root, padding=10)
frame_list.grid(row=2, column=0, columnspan=2)

ttk.Label(frame_list, text="Contact List:").pack(anchor="w")

listbox_contacts = tk.Listbox(frame_list, width=50, height=15)
listbox_contacts.pack(side="left", fill="y")
listbox_contacts.bind("<<ListboxSelect>>", display_contact_details)

scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=listbox_contacts.yview)
scrollbar.pack(side="right", fill="y")

listbox_contacts.config(yscrollcommand=scrollbar.set)

refresh_contacts()
root.mainloop()
