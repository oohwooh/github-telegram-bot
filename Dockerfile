FROM python:3.7-slim-buster

COPY requirements.txt /
RUN pip install -r requirements.txt

# /app is a subfolder that you create when you run "COPY"
COPY app.py /app/
COPY bot.py /app/
COPY github_functions /app/github_functions

WORKDIR /app
CMD ["python","bot.py"]