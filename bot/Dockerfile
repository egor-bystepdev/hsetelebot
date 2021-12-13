FROM ubuntu:18.04

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get update && apt-get install -y tesseract-ocr-all 
RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python3", "main.py"]
