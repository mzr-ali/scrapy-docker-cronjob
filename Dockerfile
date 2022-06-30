# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

# Install cron and tzdata to change time zone
RUN apt update && \
    apt-get -y install cron && \
    apt-get install tzdata -y && \
    ln -sf /usr/share/zoneinfo/Asia/Karachi /etc/localtime && \
    echo "PK/Karachi" | tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata


RUN pip install Scrapy

WORKDIR /app
COPY ../cronjob .
# copy crontab file to cron.d
COPY crontab /etc/cron.d/crontab
# give permission to crontab
RUN chmod 0644 /etc/cron.d/crontab
# Run Crontab to schedule the cron job
RUN /usr/bin/crontab /etc/cron.d/crontab
# make start script executable
RUN chmod +x start.sh

VOLUME [ "/data" ]

CMD ["./start.sh"]