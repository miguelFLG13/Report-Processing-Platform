from abc import ABC, abstractmethod

from classes.structure import Structure


class StructureRepository(ABC):
    """ Interface to extend the structure repositories """

    @abstractmethod
    def get_all(self) -> list[Structure]:
        pass
