import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import db_handler
import password_manager

db_handler.init_db()

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Password Manager")
        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Site","Username","Password"), show="headings")
        self.tree.heading("Site", text="Site")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.pack(fill=tk.BOTH, expand=True)

        add_btn = ttk.Button(self.root, text="Add", command=self.add_entry)
        add_btn.pack(side=tk.LEFT, padx=5, pady=5)

        delete_btn = ttk.Button(self.root, text="Delete", command=self.delete_entry)
        delete_btn.pack(side=tk.LEFT, padx=5, pady=5)

        gen_btn = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        gen_btn.pack(side=tk.LEFT, padx=5, pady=5)

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for entry in db_handler.get_passwords():
            id_, site, user, pwd = entry
            try:
                pwd = password_manager.decrypt_password(pwd)
            except:
                pass
            self.tree.insert("", tk.END, values=(site, user, pwd), iid=id_)

    def add_entry(self):
        site = simpledialog.askstring("Site", "Enter site name:")
        username = simpledialog.askstring("Username", "Enter username:")
        password = simpledialog.askstring("Password", "Enter password:")
        if site and username and password:
            enc_pwd = password_manager.encrypt_password(password)
            db_handler.add_password(site, username, enc_pwd)
            self.refresh_table()

    def delete_entry(self):
        selected = self.tree.selection()
        if selected:
            db_handler.delete_password(selected[0])
            self.refresh_table()

    def generate_password(self):
        pwd = password_manager.generate_password()
        messagebox.showinfo("Generated Password", pwd)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
