FROM python:3
WORKDIR /app
COPY . .
RUN pip install requests  && \
    pip install beautifulsoup4 

CMD ["python3", "futures.py"]