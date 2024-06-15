FROM python:3.12.4-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONNUNBUFFFERED 1

WORKDIR /usr/src/kwork

COPY ./DjangoProject/requirements.txt /usr/src/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements.txt

COPY ./DjangoProject/ /usr/src/kwork/

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]