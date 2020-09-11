# Readme for the Flask request layer

This request layer handles POST requests containing JSON data strings for use with psignifit-python using [Flask](https://flask.palletsprojects.com) from  e.g. JavaScript experiment libraries such as [jsPsych](https://www.jspsych.org).

## Prerequisites

- psignifit toolbox is installed

## Installation

First install Flask:
`pip3 install Flask`

Then install the CORS plugin:
`pip3 install -U flask-cors`

Also the BasicAuth plugin:
`pip3 install Flask-BasicAuth`

Then the python json schema implemention
`pip3 install jsonschema`

Ensure that the following files are in the root directory of the psignifit-python folder:
- request_layer.py
- request_layer/

Done!

## Usage

### Demo

To demo the default behaviour, run

`python3 request_layer.py`

in a terminal.

By default, the `request_layer.py` script launches a Flask server on `localhost:5000`. It is waiting for POST input at the routes defined in `request_layer.py`. It is configured to support CORS on all routes and default configuration can be found [here](https://flask-cors.corydolphin.com/en/latest/api.html#extension). It also requires authentication via basic access authentication. 

### Production
For a production run, we want to wrap things in a WGSI server. We'll use gunicorn.

#### Prerequisites

- python3
- pip3
- installation of psignifit using `setup.py`
- installation of Flask and flask-cors plugin

#### Install gunicorn

`sudo pip3 install gunicorn`

If the gunicorn command doesn't work, you might need to add it to the path, or you can execute as the path. Either way, can be found at:

`pip3 show gunicorn`

You can then run with e.g. (4 workers bound to a specific port):

`gunicorn -w 4 -b 127.0.0.1:port request_layer:app`

Replace port with the desired port, and be sure to edit the nginx config file accordingly.

#### nginx

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
