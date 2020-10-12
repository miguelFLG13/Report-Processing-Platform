from django.core.files.uploadedfile import InMemoryUploadedFile

from classes.file import PDF_CONTENT_TYPE, TXT_CONTENT_TYPE


def is_pdf_file(file: InMemoryUploadedFile):
    """ Service to check if a InMemoryUploadedFile is a Pdf """
    content_type = file.content_type

    return True if content_type == PDF_CONTENT_TYPE else False

def is_plain_text_file(file: InMemoryUploadedFile):
    """ Service to check if a InMemoryUploadedFile is a txt """
    content_type = file.content_type

    return True if content_type == TXT_CONTENT_TYPE else False
