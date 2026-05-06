import tkinter as tk
from tkinter import messagebox
from crystallinity_logic import calculate_crystallinity

def on_calc():
    try:
        p, h = poly_e.get().strip(), float(hm_e.get())
        m_val = m_e.get().strip()
        m = float(m_val) if m_val else 0.0
        
        res = calculate_crystallinity(p, h, m)
        res_l.config(text=f"Result: {res:.2f}%", fg="darkgreen")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Crystallinity v4.0")
root.geometry("300x250")

tk.Label(root, text="Polymer Name:").pack()
poly_e = tk.Entry(root)
poly_e.pack()

tk.Label(root, text="Measured Hm (J/g):").pack()
hm_e = tk.Entry(root)
hm_e.pack()

tk.Label(root, text="Moisture Content (%):").pack()
m_e = tk.Entry(root)
m_e.pack()

tk.Button(root, text="Calculate", command=on_calc).pack(pady=10)
res_l = tk.Label(root, text="", font=("Arial", 12, "bold"))
res_l.pack()

root.mainloop()
