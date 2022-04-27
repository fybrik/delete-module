FROM python:3.8-slim

ENV USER_UID=1001 \
    USER_NAME=delete-module


COPY  build/bin /usr/local/bin
RUN  /usr/local/bin/user_setup

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY ./delete-module/main.py main.py

ENTRYPOINT ["python3"]
CMD ["main.py"]

USER ${USER_UID}