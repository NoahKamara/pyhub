import tkinter as tk
from tkinter import ttk, filedialog
from pykeepass import PyKeePass
from gui import Popover
from gui.GUIComponent import GUIComponent
from os import environ


class PasswordEntry(GUIComponent[tk.Toplevel, PyKeePass]):
    _instance: tk.Toplevel
    keepass: PyKeePass | None = None
    path_entry: ttk.Entry
    password_entry: ttk.Entry

    def render(self, root: tk.Toplevel):
        self._instance = root
        frame = tk.Frame(root)

        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # KeePass database path entry and Browse button
        path_label = ttk.Label(frame, text="KeePass Database Path:")
        path_label.grid(column=0, row=0, sticky=tk.W, pady=5)

        self.path_entry = ttk.Entry(frame, width=30)
        self.path_entry.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)
        self.path_entry.insert(0, environ.get("KP_PATH"))

        browse_button = ttk.Button(frame, text="Browse", command=self.browse_file)
        browse_button.grid(column=2, row=0, pady=5, sticky=tk.W)

        # Password entry and Submit button
        password_label = ttk.Label(frame, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, pady=5)

        self.password_entry = ttk.Entry(frame, show="*", width=30)
        self.password_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
        self.password_entry.insert(0, environ.get("KP_PWD"))

        submit_button = ttk.Button(frame, text="Submit", command=self.submit_password)
        submit_button.grid(column=2, row=1, pady=5, sticky=tk.W)

        # Result label
        self.result_label = ttk.Label(frame, text="")
        self.result_label.grid(column=0, row=2, columnspan=3, pady=10)

    def output(self) -> PyKeePass:
        if self.keepass is None:
            raise Exception("Wow")

        return self.keepass

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            initialdir=".",
            title="Select KeePass Database File",
            filetypes=[("KeePass Database Files", ["*.kdbx", "*.kdb"])],
            defaultextension=".kdbx",  # Specify the default extension if not provided by the user
        )

        if file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, file_path)

    def submit_password(self):
        file_path = self.path_entry.get()
        password = self.password_entry.get()

        print("DECODING", file_path, password)
        try:
            self.keepass = PyKeePass(file_path, password=password)
            self._instance.destroy()
            self._instance.destroy()
            print("DESTROYED")

        except Exception as e:
            print(e)
            self.result_label.config(text="Error: Incorrect password or invalid KeePass file.")
