import tkinter as tk
from tkinter import ttk, messagebox


class LPTask1GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LP – Minimization Model")
        self.root.configure(bg="#f0f4ff")

        self.constraints = []

        title = tk.Label(
            root,
            text="Linear Programming ",
            font=("Arial", 20, "bold"),
            fg="#1a237e",
            bg="#f0f4ff"
        )
        title.pack(pady=10)
        obj_frame = tk.LabelFrame(
            root,
            text="Objective Function (Minimize Z)",
            padx=15,
            pady=10,
            bg="#e3f2fd",
            fg="#0d47a1",
            font=("Arial", 11, "bold")
        )
        obj_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(obj_frame, text="Z = ", font=("Arial", 12), bg="#e3f2fd").grid(row=0, column=0)

        self.c1_entry = ttk.Entry(obj_frame, width=8)
        self.c2_entry = ttk.Entry(obj_frame, width=8)

        self.c1_entry.grid(row=0, column=1)
        tk.Label(obj_frame, text="x₁  +", font=("Arial", 12), bg="#e3f2fd").grid(row=0, column=2)
        self.c2_entry.grid(row=0, column=3)
        tk.Label(obj_frame, text="x₂", font=("Arial", 12), bg="#e3f2fd").grid(row=0, column=4)
        cons_frame = tk.LabelFrame(
            root,
            text="Add Constraint",
            padx=15,
            pady=10,
            bg="#e8f5e9",
            fg="#1b5e20",
            font=("Arial", 11, "bold")
        )
        cons_frame.pack(fill="x", padx=20, pady=10)

        self.a1 = ttk.Entry(cons_frame, width=6)
        self.a2 = ttk.Entry(cons_frame, width=6)
        self.sign = ttk.Combobox(cons_frame, values=["<=", ">=", "="], width=4, state="readonly")
        self.rhs = ttk.Entry(cons_frame, width=6)

        self.sign.current(0)

        self.a1.grid(row=0, column=0)
        tk.Label(cons_frame, text="x₁  +", bg="#e8f5e9").grid(row=0, column=1)
        self.a2.grid(row=0, column=2)
        tk.Label(cons_frame, text="x₂", bg="#e8f5e9").grid(row=0, column=3)
        self.sign.grid(row=0, column=4, padx=10)
        self.rhs.grid(row=0, column=5)

        ttk.Button(cons_frame, text="Add Constraint", command=self.add_constraint).grid(row=0, column=6, padx=15)
        table_frame = tk.LabelFrame(
            root,
            text="Constraints List",
            padx=10,
            pady=10,
            bg="#fffde7",
            fg="#f57f17",
            font=("Arial", 11, "bold")
        )
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.table = ttk.Treeview(table_frame, columns=("x1", "x2", "sign", "rhs"), show="headings", height=6)

        self.table.heading("x1", text="x₁ Coef")
        self.table.heading("x2", text="x₂ Coef")
        self.table.heading("sign", text="Sign")
        self.table.heading("rhs", text="RHS")

        for col in ("x1", "x2", "sign", "rhs"):
            self.table.column(col, anchor="center", width=120)

        self.table.pack(fill="both", expand=True)

        out_frame = tk.LabelFrame(
            root,
            text="LP Formulation",
            padx=10,
            pady=10,
            bg="#fce4ec",
            fg="#880e4f",
            font=("Arial", 11, "bold")
        )
        out_frame.pack(fill="x", padx=20, pady=10)

        self.output = tk.Label(
            out_frame,
            text="",
            justify="left",
            font=("Courier New", 10),
            bg="#fce4ec"
        )
        self.output.pack(anchor="w")

        ttk.Button(root, text="Generate LP Model", command=self.display_formulation).pack(pady=12)

    def display_formulation(self):
        try:
            c1 = float(self.c1_entry.get())
            c2 = float(self.c2_entry.get())
        except:
            messagebox.showerror("Input Error", "Enter objective coefficients")
            return

        if not self.constraints:
            messagebox.showwarning("Warning", "Add at least one constraint")
            return

        text = ""
        text += "Minimize:\n"
        text += f"Z = {c1}x₁ + {c2}x₂\n\n"
        text += "Subject to:\n"

        for i, c in enumerate(self.constraints, start=1):
            text += f"C{i}: {c[0]}x₁ + {c[1]}x₂ {c[2]} {c[3]}\n"

        text += "x₁, x₂ ≥ 0"

        self.output.config(text=text)

    def add_constraint(self):
        try:
            a1 = float(self.a1.get())
            a2 = float(self.a2.get())
            sign = self.sign.get()
            rhs = float(self.rhs.get())
        except:
            messagebox.showerror("Input Error", "Enter valid constraint values")
            return

        self.constraints.append((a1, a2, sign, rhs))

        self.table.insert("", "end", values=(a1, a2, sign, rhs))

        self.a1.delete(0, tk.END)
        self.a2.delete(0, tk.END)
        self.rhs.delete(0, tk.END)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = LPTask1GUI(root)
    root.mainloop()