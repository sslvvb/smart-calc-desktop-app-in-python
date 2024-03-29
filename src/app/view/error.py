"""
Module for displaying an error message window.
"""

import customtkinter as ctk


class Error(ctk.CTkToplevel):
    """Class for displaying an error message window."""

    def __init__(self, *args, message: str, background: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x75")
        self.title("Error")
        self.resizable(False, False)
        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(padx=20, pady=20)
        self.configure(fg_color=background)
