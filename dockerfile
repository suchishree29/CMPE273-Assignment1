FROM python:2.7.13
MAINTAINER Suchishree Jena "suchishree.jena29@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]