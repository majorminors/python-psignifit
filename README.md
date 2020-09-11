# psignifit

Fork of Python toolbox for Bayesian psychometric function estimation for the [evaccum-js](https://github.com/majorminors/evaccum-js) project.

## Installation
Two methods of installation are provided by the authors of the package on the
[master branch of the Github repo](https://github.com/wichmann-lab/python-psignifit), but for development and testing, I used the [installation instructions on the wiki](https://github.com/wichmann-lab/python-psignifit/wiki/Install), which is different again. I would recommend trying that to start with. Python3 was also used during testing rather than earlier versions. Instructions modified to suit. Since the repo includes the files already, simply:

`python3 setup.py install`

This install process requires pip.

## For the Flask request layer

### Prerequisites

- psignifit toolbox is installed

### Installation

First install Flask:
`pip3 install Flask`

Then install the [flask-CORS](https://flask-cors.readthedocs.io) plugin:
`pip3 install -U flask-cors`

Also the [flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/) basic access authentication plugin:
`pip3 install Flask-HTTPAuth`

Then the python [json schema implemention](https://pypi.org/project/jsonschema/)
`pip3 install jsonschema`

Ensure that the following files are in the root directory of the psignifit-python folder:
- request_layer.py
- request_layer/

Done!

### Usage

Note, CORS support is available, but commented out. Check the `request_layer.py` to enable.

### Demo

To demo the default behaviour, run

`python3 request_layer.py`

in a terminal.

By default, the `request_layer.py` script launches a Flask server on `localhost:5000`. It is waiting for POST input at the routes defined in `request_layer.py`. It is configured to support CORS on all routes for a single ip:port and other default configuration can be found [here](https://flask-cors.corydolphin.com/en/latest/api.html#extension). It also requires authentication via basic access authentication. 

### Production
For a production run, we want to wrap things in a WGSI server. We are using gunicorn.

#### Prerequisites

- python3
- pip3
- installation of psignifit using `setup.py`
- installation of installation of request layer and dependencies

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



## Contributors

See the [CONTRIBUTORS](https://github.com/wichmann-lab/python-psignifit/blob/master/CONTRIBUTORS) file

## License and COPYRIGHT

See the [COPYRIGHT](https://github.com/wichmann-lab/python-psignifit/blob/master/COPYRIGHT) file

