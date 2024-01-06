import subprocess

from gui import GUIComponent
import tkinter as tk
from tkinter import ttk
from pykeepass import PyKeePass


class MainPage(GUIComponent[tk.Frame, ()]):
    keepass: PyKeePass

    def __init__(self, keepass: PyKeePass):
        self.keepass = keepass

    def render(self, root: tk.Frame):
        button_frame = ttk.Frame(root)
        button_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Example icons (replace with your actual icon paths)
        icon_paths = ["icon1.png", "icon2.png", "icon3.png"]

        for icon_path in icon_paths:
            icon = tk.PhotoImage(file=icon_path).subsample(3, 3)  # Adjust subsample as needed
            button = ttk.Button(button_frame, image=icon, command=self.button_clicked)
            button.image = icon  # Reference to avoid garbage collection
            button.pack(side=tk.LEFT, padx=5)

    def button_clicked(self):
        # Replace 'your_vpn_config.ovpn' with the actual path to your OpenVPN configuration file
        openvpn_command = ['sudo', 'openvpn', '--config', 'your_vpn_config.ovpn']

        # Run OpenVPN in a subprocess without blocking the main thread
        subprocess.Popen(openvpn_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("OpenVPN connection started in a subprocess.")
        print("Button clicked!")

    def output(self):
        pass
