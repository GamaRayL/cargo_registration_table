FROM node:lts
LABEL authors="Гамид"

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
