# build stage
FROM node:15.4.0-alpine3.10 as build

ENV PATH="/app/node_modules/.bin/:${PATH}"

WORKDIR /app
COPY package*.json ./

RUN npm install

COPY . /app/

# production stage
FROM nginxinc/nginx-unprivileged:1.19.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY --from=build /app/proxy/nginx.conf /etc/nginx/conf.d

COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]