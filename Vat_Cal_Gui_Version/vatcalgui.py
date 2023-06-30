import tkinter as tk

def get_percentage_input():
    percentage = entry_percentage.get()
    try:
        percentage = float(percentage)
        if percentage >= 0 and percentage <= 100:
            label_percentage_result.config(text=f"Percentage Total Entered: {percentage}")
            label_tax_result.config(text="")
            label_result.config(text="")
        else:
            label_percentage_result.config(text="Percentage must be between 0 and 100")
    except ValueError:
        label_percentage_result.config(text="Invalid input, please enter a valid percentage")

def get_amount():
    amount = entry_amount.get()
    try:
        amount = float(amount)
        if amount >= 0:
            label_amount_result.config(text="Amount Entered: {:.2f}".format(amount))
            calculate_tax()
        else:
            label_amount_result.config(text="Amount must be a positive number")
    except ValueError:
        label_amount_result.config(text="Invalid input, please enter a valid amount")

def calculate_tax():
    percentage = entry_percentage.get()
    amount = entry_amount.get()
    try:
        percentage = float(percentage)
        amount = float(amount)
        tax_calculation = amount * percentage / 100.0
        label_tax_result.config(text="The calculated VAT/SALES TAX amount on the entered amount is: {:.2f}".format(tax_calculation))
        label_result.config(text="")
    except ValueError:
        label_tax_result.config(text="Invalid input, please enter valid percentage and amount")
        label_result.config(text="")

def add_tax():
    amount = float(entry_amount.get())
    tax_calculation = float(label_tax_result.cget("text").split(": ")[1])
    result = amount + tax_calculation
    label_result.config(text="Total Amount Inclusive of VAT: {:.2f}".format(result))

def deduct_tax():
    amount = float(entry_amount.get())
    percentage = float(entry_percentage.get())
    result = amount / (1 + (percentage / 100.0))
    label_result.config(text="Total Amount Exclusive of VAT: {:.2f}".format(result))

root = tk.Tk()
root.title("VAT/SALES TAX Calculator")
root.geometry("700x700")

label_title = tk.Label(root, text="Simple Universal VAT/SALES TAX Calculator", font=("Helvetica", 16, "bold"), bg="blue", fg="yellow", padx=10, pady=10, width=80)
label_title.pack(pady=10)

frame_percentage = tk.Frame(root, bd=1, relief=tk.SOLID, padx=10, pady=10)
frame_percentage.pack(pady=10)

label_percentage = tk.Label(frame_percentage, text="Total Percentage of VAT Tax:", font=("Helvetica", 12), anchor="w")
label_percentage.grid(row=0, column=0, padx=5, pady=5)

entry_percentage = tk.Entry(frame_percentage, font=("Helvetica", 12))
entry_percentage.grid(row=0, column=1, padx=5, pady=5)

button_percentage = tk.Button(frame_percentage, text="Submit", command=get_percentage_input, bg="blue", fg="white", width=10)
button_percentage.grid(row=0, column=2, padx=5, pady=5)

label_percentage_result = tk.Label(frame_percentage, font=("Helvetica", 12), width=50)
label_percentage_result.grid(row=1, columnspan=3, padx=5, pady=5)

frame_amount = tk.Frame(root, bd=1, relief=tk.SOLID, padx=10, pady=10)
frame_amount.pack(pady=10)

label_amount = tk.Label(frame_amount, text="Amount to calculate VAT on:", font=("Helvetica", 12), anchor="w")
label_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(frame_amount, font=("Helvetica", 12))
entry_amount.grid(row=0, column=1, padx=5, pady=5)

button_amount = tk.Button(frame_amount, text="Submit", command=get_amount, bg="blue", fg="white", width=10)
button_amount.grid(row=0, column=2, padx=5, pady=5)

label_amount_result = tk.Label(frame_amount, font=("Helvetica", 12), width=50)
label_amount_result.grid(row=1, columnspan=3, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate VAT/SALES TAX", command=calculate_tax, bg="blue", fg="white", width=30)
button_calculate.pack(pady=10)

frame_result = tk.Frame(root, bd=1, relief=tk.SOLID, padx=10, pady=10)
frame_result.pack(pady=10)

label_tax_result = tk.Label(frame_result, font=("Helvetica", 12))
label_tax_result.pack()

button_add_tax = tk.Button(frame_result, text="Add VAT/SALES TAX", command=add_tax, bg="blue", fg="white", width=20)
button_add_tax.pack(pady=5)

button_deduct_tax = tk.Button(frame_result, text="Deduct VAT/SALES TAX", command=deduct_tax, bg="blue", fg="white", width=20)
button_deduct_tax.pack(pady=5)

label_result = tk.Label(frame_result, font=("Helvetica", 12))
label_result.pack(pady=10)

footer_text = "Thank you for using my Simple VAT/SALES TAX Calculator!.\n" \
              "I hope you found this tool helpful.\n" \
              "If you have any feedback or suggestions for improvement, please let me know.\n" \
              "Follow me on Github at https://github.com/Rethar-yt\n" \
              "Follow me on Linkdn at https://za.linkedin.com/in/rethar-osman-abdullah\n" \
              "Visit my website at https://roa-dev.africa\n"

label_footer = tk.Label(root, text=footer_text, font=("Helvetica", 10), anchor="center", justify="center", bg="blue", fg="white", padx=10, pady=10)
label_footer.pack(side="bottom", fill="both", padx=10, pady=10)

button_styles = {
    "bg": "#0000FF",  # Blue background color
    "fg": "white",   # White text color
}

button_percentage.configure(**button_styles)
button_amount.configure(**button_styles)
button_calculate.configure(**button_styles)
button_add_tax.configure(**button_styles)
button_deduct_tax.configure(**button_styles)


root.mainloop()
