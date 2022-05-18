FROM python:3.8-slim

ENV USER_UID=1001 \
    USER_NAME=delete-module

COPY  build/bin /usr/local/bin
RUN  /usr/local/bin/user_setup

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
COPY main.py main.py
COPY deletemodule deletemodule

ENTRYPOINT ["python3"]
CMD ["main.py"]

USER ${USER_UID}