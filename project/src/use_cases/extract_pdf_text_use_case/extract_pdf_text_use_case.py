from use_cases.extract_pdf_text_use_case.services.file_to_text_file_converter import FileToTextFileConverter
from classes.file import File


class ExtractPdfTextUseCase:
    """ Use Case to complete the text extraction in a pdf File """

    def __init__(
        self,
        file_to_text_converter: FileToTextFileConverter
    ) -> None:
        self.__file_to_text_converter = file_to_text_converter

    def extract(self, pdf_file: File) -> str:
        text_file = self.__file_to_text_converter.convert(pdf_file)
        return text_file.content
