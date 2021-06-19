FROM python:latest

WORKDIR /opt/pyfaas

COPY src /opt/pyfaas

CMD python -m pyfaas.main