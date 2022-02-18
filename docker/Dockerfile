
FROM python:3.9.2
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /opt/deploy/bezen

# Install Imagemagick
RUN apt-get update && apt-get install -y imagemagick

COPY requirements.txt $PYTHONPATH/requirements.txt
WORKDIR $PYTHONPATH
RUN pip3 install --no-cache-dir --compile -r requirements.txt
COPY . $PYTHONPATH

ENV HOME ${PYTHONPATH}
