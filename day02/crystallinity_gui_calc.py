import tkinter as tk
from tkinter import messagebox

POLYMER_DATA = {"PE": 293.0, "PP": 207.0, "PET": 140.0, "Nylon6": 230.0}

def calculate():
    try:
        poly = entry_poly.get()
        hm = float(entry_hm.get())
        if poly in POLYMER_DATA:
            xc = (hm / POLYMER_DATA[poly]) * 100
            messagebox.showinfo("Result", f"{poly} Crystallinity: {xc:.2f}%")
        else:
            messagebox.showerror("Error", "Polymer not found.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Polymer Calc")
root.geometry("300x200")

tk.Label(root, text="Polymer (PE/PP/PET):").pack(pady=5)
entry_poly = tk.Entry(root)
entry_poly.pack()

tk.Label(root, text="Measured Delta Hm (J/g):").pack(pady=5)
entry_hm = tk.Entry(root)
entry_hm.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

root.mainloop()
