FROM python:3.10.11-alpine
RUN pip install chevron==0.14.0
WORKDIR /app
COPY injector.py /app/
ENTRYPOINT ["python3","/app/injector.py"]
