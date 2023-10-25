FROM python:3.9.5

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4404

ENV FLASK_APP=app

CMD ["flask", "run", "--host=0.0.0.0", "--port=4404"]
