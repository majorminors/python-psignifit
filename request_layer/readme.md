# Readme for the Flask request layer

This request layer handles POST requests containing JSON data strings for use with psignifit-python using [Flask](https://flask.palletsprojects.com) from  e.g. JavaScript experiment libraries such as [jsPsych](https://www.jspsych.org).

## Prerequisites

- psignifit toolbox is installed

## Installation

First install Flask:
`pip3 install Flask`

Then install the CORS plugin:
`pip3 install -U flask-cors`

Ensure that the following files are in the root directory of the psignifit-python folder:
- request_layer.py
- request_layer/

Done!

## Usage

### Demo

To demo the default behaviour, run

`python3 request_layer.py`

in a terminal.

By default, the `request_layer.py` script launches a Flask server on `localhost:5000`. It is waiting for POST input at `/psignifit`. It is configured to support CORS on all routes and default configuration can be found [here](https://flask-cors.corydolphin.com/en/latest/api.html#extension). 
