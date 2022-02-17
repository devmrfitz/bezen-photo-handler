
FROM python:3.9.2
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /opt/deploy/bezen

COPY requirements.txt $PYTHONPATH/requirements.txt
WORKDIR $PYTHONPATH
RUN pip3 install --no-cache-dir --compile -r requirements.txt
COPY . $PYTHONPATH
RUN #ln -s /run/shm /dev/shm

ENV HOME ${PYTHONPATH}

EXPOSE 80
