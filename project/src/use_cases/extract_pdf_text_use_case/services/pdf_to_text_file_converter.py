from classes.file import File, PDF_CONTENT_TYPE, TXT_CONTENT_TYPE
from mocks.pdf_to_text_module import PdfToTextModuleMock

from use_cases.extract_pdf_text_use_case.services.file_to_text_file_converter import FileToTextFileConverter


class PdfToTextFileConverter(FileToTextFileConverter):
    """ Service to convert a Pdf File to a Text File """

    def convert(self, file: File) -> File:
        if not isinstance(file, File) or file.content_type != PDF_CONTENT_TYPE:
            raise TypeError

        text = PdfToTextModuleMock.convert(file)
        text_file = File(
            title="{}.txt".format(file.title),
            content_type=TXT_CONTENT_TYPE,
            content=text
        )
        return text_file
