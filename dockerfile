FROM python:3.9.5

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9404

CMD ["flask", "run", "--host=0.0.0.0","--port=9404"]
