import tkinter as tk
import math as mt
class Kalkulator():
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")

        self.entry = tk.Entry(root, width=20, font=("Arial", 18),
                            borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, pady=10)

        tombol_list = [
            ("7", 2, 3), ("8", 1, 0), ("9", 1, 1), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 1, 2),
            ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("-", 4, 0),
            ("0", 3, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("%", 1, 4)
        ]

        for (teks, baris, kolom) in tombol_list:
            if teks == "=":
                btn = tk.Button(root, text=teks, width=5, height=2,
                                font=("Arial", 14), command=self.hitung)
            else:
                btn = tk.Button(root, text=teks, width=5, height=2,
                                font=("Arial", 14),
                                command=lambda t=teks: self.click(t))
            btn.grid(row=baris, column=kolom, padx=5, pady=5)

        btn_clear = tk.Button(root, text="C", width=5, height=2,
                            font=("Arial", 14), command=self.clear, fg="red")
        btn_clear.grid(row=5, column=0, columnspan=4, sticky="nsew",
                    padx=5, pady=5)

    def click(self, tombol):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(tombol))

    def hitung(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Kalkulator(root)
    root.mainloop()