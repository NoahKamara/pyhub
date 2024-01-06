from tkinter import Tk, Frame


class Page:
    app: Tk
    title: str | None
    _frame: Frame

    def __init__(self, app: Tk, title: str | None = None):
        self.app = app
        self.title = title

    def __enter__(self) -> Frame:
        frame = Frame(self.app, borderwidth=25, bg="red")
        frame.pack(fill="both", expand=True)

        self._frame = frame
        return frame

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.app.wait_window(self._frame)