import tkinter as tk
from tkinter import messagebox, ttk
from search_and_filter import search_products

def search_gui():
    def perform_search():
        name = name_entry.get()
        category = category_entry.get()
        min_price = min_price_entry.get()
        max_price = max_price_entry.get()
        min_stock = min_stock_entry.get()
        max_stock = max_stock_entry.get()

        try:
            results = search_products(
                name=name if name else None,
                category=category if category else None,
                min_price=float(min_price) if min_price else None,
                max_price=float(max_price) if max_price else None,
                min_stock=int(min_stock) if min_stock else None,
                max_stock=int(max_stock) if max_stock else None
            )

            results_text.delete(1.0, tk.END)
            if results:
                for product in results:
                    results_text.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: {product[3]}, Stock: {product[4]}\n")
            else:
                results_text.insert(tk.END, "No products found.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for price and stock.")

    window = tk.Tk()
    window.title("Search Products")

    tk.Label(window, text="Product Name").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Category").grid(row=1, column=0)
    category_entry = tk.Entry(window)
    category_entry.grid(row=1, column=1)

    tk.Label(window, text="Min Price").grid(row=2, column=0)
    min_price_entry = tk.Entry(window)
    min_price_entry.grid(row=2, column=1)

    tk.Label(window, text="Max Price").grid(row=3, column=0)
    max_price_entry = tk.Entry(window)
    max_price_entry.grid(row=3, column=1)

    tk.Label(window, text="Min Stock").grid(row=4, column=0)
    min_stock_entry = tk.Entry(window)
    min_stock_entry.grid(row=4, column=1)

    tk.Label(window, text="Max Stock").grid(row=5, column=0)
    max_stock_entry = tk.Entry(window)
    max_stock_entry.grid(row=5, column=1)

    search_button = tk.Button(window, text="Search", command=perform_search)
    search_button.grid(row=6, column=0, columnspan=2)

    results_text = tk.Text(window, height=10, width=50)
    results_text.grid(row=7, column=0, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    search_gui()
