
## run

socketio requires a multi-threaded web-server

```
gunicorn --reload --threads 6 <filename>:<name of variable>

gunicorn --reload --threads 6 app:app
```
