# Prerequisites

- python3
- pip3
- installation of psignifit using `setup.py`
- installation of Flask and flask-cors plugin

# Install gunicorn

`sudo pip3 install gunicorn`

If the gunicorn command doesn't work, you might need to add it to the path, or you can execute as the path. Either way, can be found at:

`pip3 show gunicorn`

You can then run with e.g. (4 workers bound to a specific port):

`gunicorn -w 4 -b 127.0.0.1:port request_layer:app`

Replace port with the desired port, and be sure to edit the nginx config file accordingly.

# nginx

The minimal requirements for HTTP appear to be:

```
server {
		listen 80;
		server_name server;
		access_log  /var/log/nginx/psignifit.log;
		 
		location / {
					proxy_pass http://127.0.0.1:port;
					proxy_set_header Host $host;
					proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		}
}
```
