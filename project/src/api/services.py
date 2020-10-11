from django.core.files.uploadedfile import InMemoryUploadedFile

def is_pdf_file(file: InMemoryUploadedFile):
    """ Service to check if a InMemoryUploadedFile is a Pdf """
    content_type = file.content_type

    return True if content_type == 'application/pdf' else False
