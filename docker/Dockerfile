FROM python:3.10.11-alpine
COPY injector.py /app/
RUN pip install chevron==0.14.0
ENTRYPOINT ["python3","/app/injector.py"]