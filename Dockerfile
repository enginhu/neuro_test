FROM python:slim

RUN useradd neuro

WORKDIR /home/neuro

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY neuro_app.py test_routes.py config.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R neuro:neuro ./
USER neuro

EXPOSE 3000
ENTRYPOINT ["./boot.sh"]