FROM python:3.7

WORKDIR /app

COPY requirement.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]