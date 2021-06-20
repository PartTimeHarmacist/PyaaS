FROM python:latest

WORKDIR /opt/pyfaas

COPY src /opt/pyfaas
COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

CMD python -m pyfaas.pyfaas