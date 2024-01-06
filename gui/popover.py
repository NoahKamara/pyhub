from tkinter import Toplevel, Tk
from tkinter.ttk import Frame


class Popover:
    app: Tk
    title: str | None
    _popover: Toplevel

    def __init__(self, app: Tk, title: str | None = None):
        self.app = app
        self.title = title

    def __enter__(self) -> Toplevel:
        popover = Toplevel(self.app)

        if self.title is not None:
            popover.title(self.title)

        popover.transient(self.app)  # attach popover to main
        self.app.grab_set()  # disable inputs in main window

        self._popover = popover
        return popover

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.app.grab_release()
        self.app.wait_window(self._popover)
