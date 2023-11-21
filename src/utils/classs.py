from abc import ABC, abstractmethod



class P(ABC):
    @abstractmethod
    def move(self) -> object:
        pass


class A (P) :
    def move(self) -> object:
        print("Move")