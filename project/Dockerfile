FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
WORKDIR /src
ADD ./src /src
RUN pip install -r requirements.pip
CMD python manage.py migrate; gunicorn pdf_to_text_api.wsgi -b 0.0.0.0:80
