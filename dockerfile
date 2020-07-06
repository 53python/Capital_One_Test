FROM python:3
WORKDIR /usr/src/
COPY ./src .
RUN pip install -r requirements.txt
CMD [ "python3", "app.py"]
