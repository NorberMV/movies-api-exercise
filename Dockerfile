FROM python:slim-buster

COPY [".", "/fast-app/"]

WORKDIR /fast-app/

RUN pip install -r /fast-app/requirements.txt \
    && chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["fast-up"]
