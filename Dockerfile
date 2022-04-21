FROM python:3.10.0-alpine

VOLUME /opt/buehlerclanbot

WORKDIR /opt/buehlerclanbot

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Run the bot with unbuffered output
CMD ["python3.10", "-u", "main.py"]
