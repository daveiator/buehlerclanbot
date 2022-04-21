FROM python

VOLUME /opt/buehlerclanbot

WORKDIR /opt/buehlerclanbot

COPY . .

CMD ["python3", "main.py"]
