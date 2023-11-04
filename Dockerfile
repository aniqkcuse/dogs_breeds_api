# Builder

FROM python:3.11.6-slim-bookworm as builder

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

RUN apt-get update && \ 
	apt-get upgrade -y 

RUN pip install --upgrade pip && pip install flake8 && pip install whitenoise
COPY . /usr/bin/app/
RUN flake8 --ignore=ES501,F401 .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Final

FROM python:3.11.6-slim-bookworm

RUN mkdir -p /home/app

RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY ./start.sh .
COPY ./start_nginx.sh .

RUN sed -i 's/\r$//g' $APP_HOME/start.sh
 
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

RUN chmod +x $APP_HOME/start.sh && chmod +x $APP_HOME/start_nginx.sh

ENTRYPOINT ["/home/app/web/start.sh"]
