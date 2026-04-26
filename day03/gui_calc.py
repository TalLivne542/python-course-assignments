import tkinter as tk
from tkinter import messagebox
from crystallinity_logic import calculate_crystallinity

def run_calc():
    poly = entry_poly.get()
    try:
        hm = float(entry_hm.get())
        result = calculate_crystallinity(poly, hm)
        if result is not None:
            messagebox.showinfo("Result", f"Crystallinity: {result:.2f}%")
        else:
            messagebox.showerror("Error", "Polymer not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")

root = tk.Tk()
root.title("Crystallinity GUI")
tk.Label(root, text="Polymer:").pack()
entry_poly = tk.Entry(root)
entry_poly.pack()
tk.Label(root, text="Measured Hm:").pack()
entry_hm = tk.Entry(root)
entry_hm.pack()
tk.Button(root, text="Calculate", command=run_calc).pack()
root.mainloop()
