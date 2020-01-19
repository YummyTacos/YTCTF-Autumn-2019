FROM alpine:3.10
EXPOSE 33333

RUN apk add --no-cache gcc g++ socat

COPY tictactoe.cpp /tmp/
WORKDIR /app
RUN g++ /tmp/TicTacToe.cpp -Wall -o /app/TicTacToe -O2

ENTRYPOINT ["/usr/bin/socat", "-T", "60", "tcp-l:33333,reuseaddr,fork", "exec:/app/TicTacToe"]
