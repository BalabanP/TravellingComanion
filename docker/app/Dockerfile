FROM python:3.9


WORKDIR /workspaces


COPY requirements.txt /tmp/pip-tmp/

RUN pip3 install -r /tmp/pip-tmp/requirements.txt && rm -rf /tmp/pip-tmp
