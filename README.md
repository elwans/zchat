# Z-Chat. An SSL Secure Messenger
Locally hosted Python web-app with Jinja framework.
Templated by Winston Wijaya.

## Setup
To setup, install these packages

```bash
pip install SQLAlchemy flask-socketio simple-websocket
```

## Run
To run the app, 

```bash
gunicorn -b localhost:5000 -w 1 --keyfile cert/localhost.key --certfile cert/localhost.crt app:app
```

Since this app uses cookies, you can't open it in separate tabs to test multiple client communication. This is because cookies are shared across tabs.
You'd have to use multiple browsers to test client communication.