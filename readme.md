uses:
- reactjs
- semantic ui
- redux
- flask (gunicorn)

build semantic ui (only have to do this once)
$ cd client/semantic
$ gulp build


build client-side code
$ cd client
$ webpack -w

start server
$ cd server
$ gunicorn app:app
