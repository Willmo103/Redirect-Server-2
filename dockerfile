FROM python:3.11 as base

WORKDIR /src

COPY requirements.txt /src

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /src

ENV FLASK_APP=app

EXPOSE 9404

CMD ["flask", "run", "--host=0.0.0.0", "--port=9404"]
