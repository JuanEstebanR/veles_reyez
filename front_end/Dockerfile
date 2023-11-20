FROM node:20-alpine3.17
WORKDIR /frontend
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 9000
CMD ["npm", "run", "dev"]