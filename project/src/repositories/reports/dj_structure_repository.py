from dataclasses import asdict

from apps.reports.models import StructureModel
from classes.structure import Structure

from repositories.reports.structure_repository import StructureRepository


class DjStructureRepository(StructureRepository):
    """ Repository to manage the Structures with Django ORM """

    def get_all(self) -> list[Structure]:
        return self.__get_structure_batch(StructureModel.objects.all())

    def __get_structure(self, structure: StructureModel) -> Structure:
        return Structure(
            main_separator=structure.main_separator,
            header_separator=structure.header_separator,
            header_key_separator=structure.header_key_separator
        )

    def __get_structure_batch(self, structures: list[StructureModel]) -> list[Structure]:
        return [self.__get_structure(structure) for structure in structures]
