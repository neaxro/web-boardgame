FROM python:3.9.20-bullseye

WORKDIR /api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python", "api.py" ]
