from unittest import mock, TestCase

from apps.reports.models import StructureModel
from classes.structure import Structure
from repositories.reports.dj_structure_repository import DjStructureRepository


class TestDjStructureRepository(TestCase):
    """ Test for Django Structure Repository """

    def setUp(self) -> None:
        self.structures = [
            StructureModel("","",""),
            StructureModel("","","")
        ]
        self.structure_repository = DjStructureRepository()

    @mock.patch('repositories.reports.dj_structure_repository.StructureModel')
    def test_get_all_correct(self, mock_model) -> None:
        """ Test method get_all in a valid environment """
        mock_model.objects.all.return_value = [
            StructureModel("","",""),
            StructureModel("","","")
        ]

        structures = self.structure_repository.get_all()
        self.assertEqual(len(self.structures), len(structures))
