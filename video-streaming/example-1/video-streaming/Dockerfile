FROM node:latest

WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Update npm to the latest version
RUN npm install -g npm@10.4.0

# Install project dependencies
RUN npm install

# Copy the application code
COPY ./src ./src
COPY ./videos ./videos

# Expose port 4000
EXPOSE 4000

# Set default port if not provided
ENV PORT=4000

# Start the application on port 4000
CMD npm start

