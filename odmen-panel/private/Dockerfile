FROM node:10.16.3-alpine

COPY . /app
RUN npm i

ENTRYPOINT ["/usr/local/bin/node", "/app/server.js"]
