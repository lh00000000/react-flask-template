uses:
- reactjs
- semantic ui
- redux
- flask (gunicorn)

npm install clientside code (only have to do this once)
$ cd client
$ npm install

build semantic ui (only have to do this once)
$ cd client/semantic
$ gulp build

dev client_side
$ cd client
$ webpack-dev-server --content-base ..
# go to http://0.0.0.0:8080/webpack-dev-server/
# navigate to server/dev-index

build client-side code
$ cd client
$ webpack -w

start server
$ cd server
$ gunicorn app:app
