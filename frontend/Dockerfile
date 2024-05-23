FROM node:20.11.1-alpine

ENV NODE_ENV=production

WORKDIR /usr/src/app

COPY package.json /usr/src/app/

RUN npm install

COPY . .

CMD [ "npm", "start" ]