import tkinter as tk
from tkinter import messagebox
from subprocess import run
import os

import investment_equations_utils as utils

class CapitalGainCalculatorGUI:
    def __init__(self, master):
        self.master = master
        
        self.title = "Investment Calculator"
        master.title(self.title)
        
        logo_path = os.path.join("images", "pf_calculator_logo.png")
        self.logo = tk.PhotoImage(file=logo_path)
        master.wm_iconphoto(True, self.logo)

        self.font_style = ("Arial", 12)
        self.title_font_style = ("Segoe UI", 18)

        # for i in range(6):
        #     self.master.grid_rowconfigure(i, weight=1)
        #     self.master.grid_columnconfigure(i, weight=1)

        self.frame = None
        self.menu_bar = None
        self.create_home_page()
        
    def create_home_page(self):
        
        if self.frame:
            for widget in self.frame.winfo_children():
                widget.destroy()
                
        if self.menu_bar:
            self.menu_bar.destroy()
        
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.home_logo = tk.Label(self.frame, image=self.logo)
        self.home_logo.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.home_title = tk.Label(self.frame, text='Welcome to Investement Calculator', font=self.title_font_style, bg='white', padx=10, pady=5)
        self.home_title.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.investment_return_button = tk.Button(self.frame, text="Calculate Investment Return", command=lambda : [self.create_menu_bar(), self.create_widgets_accrued()], font=self.font_style, bg="#74FE8D", fg="black", padx=10, pady=5)
        self.investment_return_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.start_amount_button = tk.Button(self.frame, text="Calculate Start Amount", command=lambda : [self.create_menu_bar(), self.create_widgets_target()], font=self.font_style, bg="#74FE8D", fg="black", padx=10, pady=5)
        self.start_amount_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ns")
        
        self.start_amount_button = tk.Button(self.frame, text="Open Calculator", command=self.open_calculator, font=self.font_style, bg="#74FE8D", fg="black", padx=10, pady=5)
        self.start_amount_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="ns")
        
    def open_calculator(self):
        if os.name == 'posix':
            run(["/usr/bin/gnome-calculator"])
        elif os.name == 'nt':
            run(["calc.exe"])

    def create_menu_bar(self):
        self.menu_bar = tk.Menu(self.master, background='#74FE8D')
        self.master.config(menu=self.menu_bar)

        self.calculation_menu = tk.Menu(self.menu_bar, tearoff=0, activebackground='#74FE8D')
        self.calculation_menu.add_command(label="Home", command=self.create_home_page)
        self.calculation_menu.add_separator()
        self.calculation_menu.add_command(label="Calculate Investment Return", command=self.create_widgets_accrued)
        self.calculation_menu.add_command(label="Calculate Start Amount", command=self.create_widgets_target)
        self.menu_bar.add_cascade(label="Equation", menu=self.calculation_menu, background='#74FE8D')

    def create_widgets_accrued(self):
        
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        self.principal_label = tk.Label(self.frame, text="Principal Amount ($):", font=self.font_style, bg='white')
        self.principal_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.principal_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.principal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.rate_label = tk.Label(self.frame, text="Annual Return Rate (%):", font=self.font_style, bg='white')
        self.rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rate_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.rate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.years_label = tk.Label(self.frame, text="Number of Years:", font=self.font_style, bg='white')
        self.years_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.years_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.years_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.calculate_button = tk.Button(self.frame, text="Calculate", command=self.calculate_accrued_amount, font=self.font_style, bg="#74FE8D", fg="black", padx=10, pady=5)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.frame, text="", font=self.font_style, bg='white')
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)
        
    def create_widgets_target(self):
        
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        self.principal_label = tk.Label(self.frame, text="Target Amount ($):", font=self.font_style, bg='white')
        self.principal_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.principal_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.principal_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        self.rate_label = tk.Label(self.frame, text="Annual Return Rate (%):", font=self.font_style, bg='white')
        self.rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rate_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.rate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.years_label = tk.Label(self.frame, text="Number of Years:", font=self.font_style, bg='white')
        self.years_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.years_entry = tk.Entry(self.frame, font=self.font_style, bg="#74FE8D", fg="black")
        self.years_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        self.calculate_button = tk.Button(self.frame, text="Calculate", command=self.calculate_principal_given_target, font=self.font_style, bg="#74FE8D", fg="black", padx=10, pady=5)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.frame, text="", font=self.font_style, bg='white')
        self.result_label.grid(row=4, column=0, columnspan=2, pady=5)

    def calculate_accrued_amount(self):
        try:
            principal_amount = int(self.principal_entry.get())
            annual_return_rate = int(self.rate_entry.get())
            years = int(self.years_entry.get())

            capital_gain = utils.accrued_amount(principal_amount, annual_return_rate, years)
            self.result_label.config(text=f"Capital Gain: {capital_gain:,.2f} $")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid input.")

    def calculate_principal_given_target(self):
        try:
            target_amount = int(self.principal_entry.get())
            annual_return_rate = int(self.rate_entry.get())
            years = int(self.years_entry.get())

            principal_amount = utils.principal_amount_given_target(target_amount, annual_return_rate, years)
            self.result_label.config(text=f"Principal Amount: {principal_amount:,.2f} $")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid input.")

def main():
    app_title = "Investment Calculator"
    root = tk.Tk(className=app_title)
    CapitalGainCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
