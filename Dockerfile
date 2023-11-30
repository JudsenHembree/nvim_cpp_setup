FROM xianpengshen/clang-tools:12

#install clang make and cmake
RUN apt-get update && apt-get install -y \
    clang \
    python3 

WORKDIR /tmp
COPY . .

RUN python3 ./rework.py

CMD [ "" ]
