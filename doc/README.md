## Doc

I've tried to use hexagonal architecture and DDD in the project.

In folder `project/src` we have some folders:

- **api**: In our infrastructure we have the API REST developed with Django REST Framework and it is in this folder
- **apps**: We need to communicate with our DB and we need something in our infrastructure. In this case we use the Django Orm and we need the models and the migrations..
- **classes**: The entities of our domain.
- **mocks**: Manual mocks to simulate some behaviors.
- **project_config**: Django project configuration.
- **repositories**: We want to have another abstraction layer to not couple with Django. The repositories that help to do that are here.
- **use_cases**: Our use_cases that resolve our functionality in our application layer.

### Exercise 1

I implemented a endpoint to upload a pdf doc and return the content as a string.

I used the module named pypendency to helps me to the dependencies injection in python configuring the yamls in _dependecy folders and loading in \_\_init\_\_.py in src folder.

I developed only one class in classes folder:

- **File**:  Class to represent a file in the project.

In this case I developed extract_pdf_text_use_case and some services to get the goal: file_to_text_file_converter and pdf_to_text_file_converter.

- **file_to_text_file_converter**: It's the interface for converters to text.
- **pdf_to_text_file_converter**: It's the concrete class that inherits from file_to_text_file_converter to return a text File giving a pdf.
- **extract_pdf_text_use_case**: Use case that, giving a pdf file, gets the text of that pdf.

I thought in create a extra abstraction layer after pdf_to_text_file_converter named mock_pdf_to_text_file_converter to use the mock to convert the pdf but it's a test exercise and it give too much complexity.

Finally I implemented the endpoint named PdfToTextAPIView in api/views.

To simulate the behavior of the pdf converter I defined a stupid mock named pdf_to_text_module in the folder mocks.

Tests folders replicate the structure of the main folder with the tests of each file.

### Exercise 2

I supposed that we send a txt file with a structure divided by the same separator to get the headers, the text and the footer, and in the header we have some variables divided by a separator and each variable has the key and the value divided by another separator. Example: header=123|cool text|footer

I developed 2 new classes:

- **Report**:  The representation of a report with the patient_id and the document_text. Open to extend.
- **Structure**: This represent a structure of the files to apply in a regex. This concept must be introduced before, in this case, this is persisted in the database.

And we needed to persist the data, this implied I implemented a Django app with the models ReportModel and StructureModel, and It was necessary developed the repositories:

- **report_repository**: Interface to extend the repository with different tools to get the reports data.
- **dj_report_repository**: Repository that extends the report_repository to get the reports data in a database with django.
- **structure_repository**: Interface to extend the repository with different tools to get the structures data.
- **dj_structure_repository**: Repository that extends the structure_repository to get the structures data in a database with django.

In this case I developed get_report_information_use_case and some services to get the goal: report_information_processor and regex_report_information_processor.

- **report_information_processor**: It's the interface for processors of text reports.
- **report_information_processor**: It's the concrete class that inherits from report_information_processor to return a Report giving a text file.
- **get_report_information_use_case**: Use case that, giving a text file, gets the Report and persist the information.

Finally I implemented the endpoint named ProcessReportAPIView in api/views.

I thought in implement a custom exception to raise when not look for a correct structure but finally I didn't have enough time and I put simply Exception.

Sorry but:

- I wanted to hash the patient_id but finally I didn't it.
- I didn't complete the tests for ProcessReportAPIView because I didn't have more time, but more or less is the same than the other test class.


For more details: ask me ;)


