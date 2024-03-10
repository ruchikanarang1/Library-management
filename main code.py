import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta
from tkcalendar import DateEntry
from PIL import ImageTk,Image


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.background_image = Image.open("bgfort.jpeg")  
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.create_widgets()

        self.books = {}
        self.borrowed_books = {}

        self.create_widgets()

    def create_widgets(self):
        canvas = tk.Canvas(self.root, width=800, height=600)
        canvas.place(x=0,y=0)
        canvas.create_image(0, 0, image=self.background_photo, anchor=tk.NW)

        tk.Label(self.root, text="Book Title").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Quantity").grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Cost").grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Issue Date ").grid(row=0, column=3, padx=10, pady=10)
        tk.Label(self.root, text="Return Date ").grid(row=0, column=4, padx=10, pady=10)



        # Entry fields
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=1, column=0, padx=10, pady=10)

        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.cost_entry = tk.Entry(self.root)
        self.cost_entry.grid(row=1, column=2, padx=10, pady=10)

        self.issue_entry =DateEntry(self.root,datepattern="yyyy-mm-dd")
        self.issue_entry.grid(row=1, column=3, padx=10, pady=10)

        self.return_entry =DateEntry(self.root,datepattern="yyyy-mm-dd")
        self.return_entry.grid(row=1, column=4, padx=10, pady=10)


        # Buttons
        tk.Button(self.root, text="Add Book", command=self.add_book).grid(row=3, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Borrow Book", command=self.borrow_book).grid(row=4, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Return Book", command=self.return_book).grid(row=5, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Show Borrowed Books", command=self.show_borrowed_books).grid(row=6, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Check Availability", command=self.check_availability).grid(row=7, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Reserve Book", command=self.reserve_book).grid(row=8, column=3, padx=10, pady=10)

        
    def add_book(self):
        title = self.title_entry.get()
        quantity = int(self.quantity_entry.get())
        cost = float(self.cost_entry.get())

        if title and quantity > 0:
            self.books[title] = {'quantity': quantity, 'cost': cost}
            messagebox.showinfo("Success", f"Added {quantity} copies of '{title}' to the library.")
        else:
            messagebox.showerror("Error", "Invalid input.")

    def borrow_book(self):
        title = self.title_entry.get()
        issue_date=self.issue_entry.get()
        return_date=self.return_entry.get()

        if title in self.books:
            if self.books[title]['quantity'] > 0:
                self.books[title]['quantity'] -= 1
                self.borrowed_books[title] = {'issue_date': f"'{issue_date}'", 'return_date': f"'{return_date}'", 'fine': 0.0}
                messagebox.showinfo("Success", f"Borrowed '{title}'.")
            else:
                messagebox.showerror("Error", f"'{title}' is out of stock.")
        else:
            messagebox.showerror("Error", f"'{title}' not found in the library.")

    def return_book(self):
        title = self.title_entry.get()

        if title in self.borrowed_books:
            self.books[title]['quantity'] += 1
            del self.borrowed_books[title]
            messagebox.showinfo("Success", f"Returned '{title}'.")
        else:
            messagebox.showerror("Error", f"'{title}' not borrowed.")

    def show_borrowed_books(self):
        if self.borrowed_books:
            borrowed_list = "\n".join(self.borrowed_books.keys())
            messagebox.showinfo("Borrowed Books", f"Borrowed Books:\n{borrowed_list}")
        else:
            messagebox.showinfo("Borrowed Books", "No books are currently borrowed.")

    def check_availability(self):
        title = self.title_entry.get()

        if title in self.books:
            quantity = self.books[title]['quantity']
            messagebox.showinfo("Availability", f"'{title}' is available. Quantity: {quantity}")
        else:
            messagebox.showerror("Availability", f"'{title}' not found in the library.")

    def reserve_book(self):
        title = self.title_entry.get()

        if title in self.books:
            if self.books[title]['quantity'] == 0:
                self.books[title]['reserved'] = True
                messagebox.showinfo("Reserved", f"'{title}' is reserved for you.")
            else:
                messagebox.showinfo("Reserved", f"'{title}' is available. No need to reserve.")
        else:
            messagebox.showerror("Error", f"'{title}' not found in the library.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
