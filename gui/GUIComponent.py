from abc import abstractmethod, ABC
from typing import TypeVar

Root = TypeVar('Root')
Output = TypeVar('Output')


class GUIComponent[Root, Output]:
    @abstractmethod
    def render(self, root: Root):
        pass

    @abstractmethod
    def output(self) -> Output:
        pass
