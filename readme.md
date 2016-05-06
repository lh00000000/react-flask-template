uses:
- reactjs
- semantic ui
- redux
- flask (gunicorn)

npm install clientside code (only have to do this once)
------
```bash
$ cd client
$ npm install
```

build semantic ui (only have to do this once)
------
```bash
$ cd client/semantic
$ gulp build
```

dev client_side
------
```bash
$ cd client
$ webpack-dev-server --content-base .. --inline --hot
```
go to http://0.0.0.0:8080/webpack-dev-server/
navigate to server/dev-index

build client-side code
------
```bash
$ cd client
$ webpack -w
```

start server
------
```bash
$ cd server
$ gunicorn app:app
```
