FROM node:14

WORKDIR /app
# Instalamos dependencias
COPY package.json package-lock.json ./
RUN npm install
# Copiamos los archivos de la nuestra aplicacion
COPY . .
# Exponemos el puerto 3000
EXPOSE 3000
# Iniciar la aplicación Next.js
CMD ["npm", "run", "dev"]