FROM python:3.8

RUN mkdir -p /app/src

WORKDIR /app/src
COPY . .

RUN apt-get -y update && apt-get install -y libsndfile1

RUN pip install numpy && \
    pip install matplotlib && \
    pip install soundfile
# RUN sed $'s/\r$//' ./install.sh > ./install.Unix.sh
# RUN chmod +x install.Unix.sh
RUN ./install.sh
# Start

CMD [ "python", "examples/example.py" ]