import tkinter as tk
from tkinter import messagebox

# Banka hesapları (Geçici olarak listede tutuluyor, veritabanına geçilebilir)
customer_accounts = [
    {
        "name": "Betül",
        "surname": "Yazıcı",
        "accountNumber": 1,
        "balance": 150000,
        "additionalAccount": 5000,
        "username": "betulYazici",
        "password": "1234"
    },
    {
        "name": "Cansu",
        "surname": "İnam",
        "accountNumber": 2,
        "balance": 5000,
        "additionalAccount": 2000,
        "username": "inamCansu",
        "password": "4321"
    }
]

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Application")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to ATM", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Label(self.root, text="Username:", bg="#f0f0f0").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password:", bg="#f0f0f0").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", command=self.login, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        for account in customer_accounts:
            if account['username'] == username and account['password'] == password:
                self.account = account
                self.create_main_menu()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome {self.account['name']}", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(self.root, text="Balance Inquiry", command=self.balance_inquiry, width=20, height=2, bg="#008CBA", fg="white").pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money, width=20, height=2, bg="#FF9800", fg="white").pack(pady=5)
        tk.Button(self.root, text="Deposit Money", command=self.deposit_money, width=20, height=2, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.create_login_screen, width=20, height=2, bg="#f44336", fg="white").pack(pady=5)

    def balance_inquiry(self):
        messagebox.showinfo("Balance", f"Account Balance: {self.account['balance']} liras\nAdditional Account: {self.account['additionalAccount']} liras")

    def withdraw_money(self):
        self.clear_window()
        tk.Label(self.root, text="Enter amount to withdraw:", bg="#f0f0f0").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Withdraw", command=self.process_withdraw, bg="#FF9800", fg="white").pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg="#4CAF50", fg="white").pack(pady=5)

    def process_withdraw(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Invalid Amount")
            if self.account['balance'] >= amount:
                self.account['balance'] -= amount
                messagebox.showinfo("Success", "Withdrawal successful.")
            elif self.account['balance'] + self.account['additionalAccount'] >= amount:
                use_additional = messagebox.askyesno("Additional Account", "Insufficient balance. Use additional account?")
                if use_additional:
                    remaining = amount - self.account['balance']
                    self.account['balance'] = 0
                    self.account['additionalAccount'] -= remaining
                    messagebox.showinfo("Success", "Withdrawal successful using additional account.")
            else:
                messagebox.showerror("Error", "Insufficient balance.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def deposit_money(self):
        self.clear_window()
        tk.Label(self.root, text="Enter amount to deposit:", bg="#f0f0f0").pack(pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        tk.Button(self.root, text="Deposit", command=self.process_deposit, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg="#FF9800", fg="white").pack(pady=5)

    def process_deposit(self):
        try:
            amount = int(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Invalid Amount")
            self.account['balance'] += amount
            messagebox.showinfo("Success", "Deposit successful.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the application
root = tk.Tk()
atm = ATMApp(root)
root.mainloop()
