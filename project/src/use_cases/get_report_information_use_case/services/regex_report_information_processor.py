import re
from datetime import datetime

from classes.file import File, TXT_CONTENT_TYPE
from classes.report import Report
from repositories.reports.structure_repository import StructureRepository

from use_cases.get_report_information_use_case.services.report_information_processor import ReportInformationProcessor


class RegexReportInformationProcessor(ReportInformationProcessor):
    """ Service to process the information of a text file with regexs """

    def __init__(
        self,
        structure_repository: StructureRepository
    ) -> None:
        self.__structure_repository = structure_repository

    def process(self, text_file: File) -> Report:
        if (
            not isinstance(text_file, File) or
            text_file.content_type != TXT_CONTENT_TYPE
        ):
            raise TypeError

        document_text = None
        headers = {}

        structures = self.__structure_repository.get_all()
        for structure in structures:
            main_separator = structure.main_separator
            processed_text = re.split(main_separator, text_file.content)
            document_text = processed_text[1]
            header_separator = structure.header_separator

            headers = {}
            for header in re.split(header_separator, processed_text[0]):
                header_key_separator = structure.header_key_separator
                header_dict = re.split(header_key_separator, header)
                headers[header_dict[0]] = header_dict[1]

            if document_text and 'patient_id' in headers:
                break

        if not document_text or not headers.get('patient_id'):
            raise Exception("Unknow Structure")

        return Report(
            created_at=datetime(2020,10,12,13,0,0),
            patient_id=headers['patient_id'],
            document_text=document_text
        )
