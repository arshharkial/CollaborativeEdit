
## run

socketio requires a multi-threaded web-server

```
gunicorn --threads 6 <filename>:<name of variable>

gunicorn --threads 6 app:app
```
