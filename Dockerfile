FROM python:slim

RUN mkdir -p /python
COPY main.py /python
COPY app.py /python
COPY discord.py /python
COPY twitch.py /python
COPY requirements.txt /python


WORKDIR /python
RUN pip install -r requirements.txt
CMD ["python3", "-u", "main.py"]