FROM python:3.9

RUN useradd -m bot

COPY main.py /home/bot/main.py

USER bot

RUN pip install --user pytelegrambotapi

CMD python /home/bot/main.py
