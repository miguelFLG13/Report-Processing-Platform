from django.db import models


class StructureModel(models.Model):
    main_separator = models.CharField(max_length=20)
    header_separator = models.CharField(max_length=20)
    header_key_separator = models.CharField(max_length=20)


class ReportModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient_id = models.CharField(max_length=50)
    document_text = models.TextField()
