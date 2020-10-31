FROM python:alpine3.7
COPY . /hello-flask
WORKDIR /hello-flask
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3 ./hello.py