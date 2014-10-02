web: gunicorn -b $BIND:$PORT -k eventlet application.hello:app
test: python tests/hello.py
