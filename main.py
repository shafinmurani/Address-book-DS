import tkinter as tk
from tkinter import messagebox


class Record:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.next = None


class TelephoneDirectory:
    def __init__(self):
        self.head = None

    def add_record(self, name, phone_number, address):
        new_record = Record(name, phone_number, address)
        new_record.next = self.head
        self.head = new_record
        messagebox.showinfo("Success", "Record added successfully.")

    def search_record(self, name):
        current = self.head
        while current:
            if current.name == name:
                info = f"Name: {current.name}\nPhone Number: {current.phone_number}\nAddress: {current.address}"
                messagebox.showinfo("Record Found", info)
                return
            current = current.next
        messagebox.showinfo("Record Not Found", "Record not found.")

    def modify_record(self, name, new_phone_number, new_address):
        current = self.head
        while current:
            if current.name == name:
                current.phone_number = new_phone_number
                current.address = new_address
                messagebox.showinfo("Success", "Record modified successfully.")
                return
            current = current.next
        messagebox.showinfo("Record Not Found", "Record not found.")

    def list_records(self):
        current = self.head
        info = "Telephone Directory:\n"
        while current:
            info += (f"\nName: {current.name}\nPhone Number: {current.phone_number}\nAddress: {current.address}\n"
                     f"-----------------------")
            current = current.next
        messagebox.showinfo("List Records", info)

    def delete_record(self, name):
        current = self.head
        prev = None

        while current:
            if current.name == name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                messagebox.showinfo("Success", "Record deleted successfully.")
                return
            prev = current
            current = current.next

        messagebox.showinfo("Record Not Found", "Record not found.")


class TelephoneDirectoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Telephone Directory System")
        self.root.geometry("500x400")

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width - 500) / 2)
        y_coordinate = int((screen_height - 400) / 2)
        self.root.geometry(f"500x400+{x_coordinate}+{y_coordinate}")

        self.directory = TelephoneDirectory()

        self.label_name = tk.Label(root, text="Name:")
        self.label_phone_number = tk.Label(root, text="Phone Number:")
        self.label_address = tk.Label(root, text="Address:")

        self.entry_name = tk.Entry(root, width=30)
        self.entry_phone_number = tk.Entry(root, width=30)
        self.entry_address = tk.Entry(root, width=30)

        self.button_add = tk.Button(root, text="Add Record", command=self.add_record, width=15)
        self.button_search = tk.Button(root, text="Search Record", command=self.search_record, width=15)
        self.button_modify = tk.Button(root, text="Modify Record", command=self.modify_record, width=15)
        self.button_list = tk.Button(root, text="List Records", command=self.list_records, width=15)
        self.button_delete = tk.Button(root, text="Delete Record", command=self.delete_record, width=15)

        # Align labels and entry boxes in a row
        label_entry_pairs = [
            (self.label_name, self.entry_name),
            (self.label_phone_number, self.entry_phone_number),
            (self.label_address, self.entry_address)
        ]

        for label, entry in label_entry_pairs:
            label.grid(row=label_entry_pairs.index((label, entry)), column=0, padx=10, pady=10, sticky=tk.E)
            entry.grid(row=label_entry_pairs.index((label, entry)), column=1, padx=10, pady=10, sticky=tk.W)

        # Align buttons in a column
        for button in (self.button_add, self.button_search, self.button_modify, self.button_list, self.button_delete):
            button.grid(columnspan=2, pady=10)

        # Configure column weights to center content
        for col in range(2):  # Two columns in this layout
            root.columnconfigure(col, weight=1)

    def add_record(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone_number.get()
        address = self.entry_address.get()
        if name and phone_number and address:
            self.directory.add_record(name, phone_number, address)
            self.clear_entries()
        else:
            messagebox.showwarning("Invalid Input", "Please fill in all fields.")

    def search_record(self):
        name = self.entry_name.get()
        if name:
            self.directory.search_record(name)
            self.clear_entries()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a name.")

    def modify_record(self):
        name = self.entry_name.get()
        new_phone_number = self.entry_phone_number.get()
        new_address = self.entry_address.get()
        if name:
            self.directory.modify_record(name, new_phone_number, new_address)
            self.clear_entries()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a name.")

    def list_records(self):
        self.directory.list_records()

    def delete_record(self):
        name = self.entry_name.get()
        if name:
            self.directory.delete_record(name)
            self.clear_entries()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a name.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone_number.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)


def main():
    root = tk.Tk()
    TelephoneDirectoryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
