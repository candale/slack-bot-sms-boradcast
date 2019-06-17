FROM python:3.6

RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential

EXPOSE 5000

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt


COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
