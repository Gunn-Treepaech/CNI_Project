FROM node:latest

WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the application code
COPY ./src ./src
COPY ./videos ./videos

ENV PORT 80
ENV RABBIT amqp://guest:guest@rabbit:5672
ENV NODE_ENV development

EXPOSE 80

CMD npx wait-port rabbit:5672 && \
    npm start

# docker run -p 4001:80 <your_image_name>
