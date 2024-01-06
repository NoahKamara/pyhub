import tkinter
from tkinter import Tk, Toplevel
from tkinter.ttk import Frame
from typing import Callable

from .page import Page
from .popover import Popover
from .GUIComponent import GUIComponent

class App(Tk):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mainloop()

    def popover[T](self, component: GUIComponent[tkinter.Toplevel, T]) -> T:
        with Popover(self) as pop:
            component.render(root=pop)
        return component.output()

    def frame[T](self, component: GUIComponent[tkinter.Frame, T]) -> T:
        with Page(self) as pop:
            component.render(root=pop)
        return component.output()

    # def popover[T](self, title: str, callback: Callable[[Frame], T]) -> T:
    #     with Popover(self, title=title) as pop:
    #         return callback(pop)

    def start(self):
        self.mainloop()
