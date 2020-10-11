from abc import ABC, abstractmethod

from classes.file import File


class FileToTextFileConverter(ABC):
    """ Interface to extend the converters by type of file to text File """

    @abstractmethod
    def convert(self, file: File) -> File:
        pass
