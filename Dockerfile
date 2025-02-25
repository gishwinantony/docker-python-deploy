FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY  ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY /Learning /code/Learning

WORKDIR /code/Learning

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]