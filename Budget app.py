import tkinter as tk
from tkinter import messagebox #error messages
import json   #saving data
from datetime import datetime

class BudgetApp:  #reusable/more organized
    def __init__(self, root):  #Initializes budget app bc it's a class
        self.balance = 0.0   #uses self so it can exist outside the function
        self.transactions = []  #Doesn't have to be a list but is the easiest way to store and display transactions.
        
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#2C3E50")
        
        self.load_data()
        
        # Balance Label
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance:.2f}", font=("Arial", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.balance_label.pack(pady=10)
        
        #Income section
        tk.Label(root, text="Add Income:", font=("Arial", 12), fg="#1ABC9C", bg="#2C3E50").pack() #income label
        self.income_entry = tk.Entry(root, font=("Arial", 12), bg="#ECF0F1") 
        self.income_entry.pack()
        tk.Label(root, text="Description:", font=("Arial", 10), fg="#BDC3C7", bg="#2C3E50").pack()
        self.income_desc = tk.Entry(root, font=("Arial", 12), bg="#ECF0F1")
        self.income_desc.pack()
        tk.Button(root, text="Add Income", command=self.add_income, font=("Arial", 12), fg="#FFFFFF", bg="#27AE60").pack(pady=5)
        
        # Expense Section
        tk.Label(root, text="Add Expense:", font=("Arial", 12), fg="#E74C3C", bg="#2C3E50").pack()
        self.expense_entry = tk.Entry(root, font=("Arial", 12), bg="#ECF0F1")
        self.expense_entry.pack()
        tk.Label(root, text="Description:", font=("Arial", 10), fg="#BDC3C7", bg="#2C3E50").pack()
        self.expense_desc = tk.Entry(root, font=("Arial", 12), bg="#ECF0F1")
        self.expense_desc.pack()
        tk.Button(root, text="Add Expense", command=self.add_expense, font=("Arial", 12), fg="#FFFFFF", bg="#C0392B").pack(pady=5)
        
        # Transaction History
        tk.Label(root, text="Transactions:", font=("Arial", 12), fg="#F1C40F", bg="#2C3E50").pack()
        self.transactions_text = tk.Text(root, height=10, width=40, font=("Arial", 10), bg="#34495E", fg="#ECF0F1")
        self.transactions_text.pack()
        
        
    def add_income(self):
        try:
            income = float(self.income_entry.get())
            desc = self.income_desc.get() or "Income"
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.balance = self.balance + income
            self.transactions.append(f"{date} - {desc}: +${income:.2f}")  #saves transactions
            self.update_ui()
            self.save_data()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
    
    def add_expense(self):
        try:
            expense = float(self.expense_entry.get())
            desc = self.expense_desc.get() or "Expense"
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if expense > self.balance:
                messagebox.showerror("Error", "Insufficient funds!")
            else:
                self.balance = self.balance - expense
                self.transactions.append(f"{date} - {desc}: -${expense:.2f}")
                self.update_ui()
                self.save_data()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
    
    def update_ui(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        self.transactions_text.delete(1.0, tk.END) #clears old transactions
        for transaction in self.transactions:
            self.transactions_text.insert(tk.END, transaction + "\n")
    
    def save_data(self):
        data = {"balance": self.balance, "transactions": self.transactions}
        with open("budget_data.json", "w") as file:
            json.dump(data, file)
    
    def load_data(self):
        try:
            with open("budget_data.json", "r") as file:
                data = json.load(file)
                self.balance = data.get("balance", 0.0)  #loads balance
                self.transactions = data.get("transactions", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.balance = 0.0
            self.transactions = []
        
if __name__ == "__main__":   #only runs directly from python file
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop() #runs app until x is pressed
