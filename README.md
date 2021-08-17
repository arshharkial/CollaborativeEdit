
## run

socketio requires a multi-threaded web-server

- use eventlet asynchronous web server and run it with gunicorn eventlet worker
- The eventlet worker does not need multiple worker
- It handles multiple connection via asynchronous support is able to handle thousands of connections

```
gunicorn -k eventlet -w 1 --reload app:app
```

In case of

> Gunicorn ImportError: cannot import name 'ALREADY_HANDLED' from 'eventlet.wsgi' in docker

switch to older version of eventlet solved the problem i.e. `pip install eventlet==0.30.2`