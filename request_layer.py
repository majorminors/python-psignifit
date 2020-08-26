from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from jsonschema import validate
import numpy as np
import psignifit as ps

app = Flask(__name__, root_path='request_layer/') # make Flask look in the 'request_layer/' dir for templates etc, instead of in the root dir
CORS(app)

#@app.route('/')
#def output(): # serve the demo script
#    return render_template('demo.html')

@app.route("/pyapps/util/cthresh", methods=['POST'])
def calculate_coh():
    if request.get_json() is None: # abort if not JSON (sanitise input)
        abort(400)
    elif request.content_length is not None and request.content_length > 1024: # let's also limit the size of permitted payloads to 1 KB
        abort(413)
    else: # if JSON, continue
        received_data = request.get_json() # pull the data out of the POST request

        # now use jsonschema to validate
        validate(received_data, {"maxItems": 1}) # check only one item
        valid_schema_object = { # check that the object is correctly formatted
                "type": "object", # its an object
                "properties": {
                    "data_array": { # called 'data_array'
                        "type" : "array", # that is an array
                        "items": {
                            "type": "array", # consisting of arrays
                            "items": {
                                "type": "number" # which have only numbers inside
                            }
                        }
                    },
                },
                "required": ["data_array"], # 'data_array' is required
                "additionalProperties": False # and nothing else exists in the object
        }
        validate(received_data,valid_schema_object)

        converted_data = received_data['data_array'] # format of the POST comes in as a dict, so just select the array

        # set up psignifit with some standard options
        options = dict();
        options['sigmoidName'] = 'norm';
        options['expType']     = '2AFC';

        options['threshPC']    = 0.9;
        result_upper = ps.psignifit(converted_data,options);
        options['threshPC']    = 0.7;
        result_lower = ps.psignifit(converted_data,options);

        thresholds = [result_upper['Fit'][0],result_lower['Fit'][0]]

        return jsonify(thresholds)

@app.route("/pyapps/util/rthresh", methods=['POST'])
def calculate_rule():
    if request.get_json() is None: # abort if not JSON (sanitise input)
        abort(400)
    elif request.content_length is not None and request.content_length > 1024: # let's also limit the size of permitted payloads to 1 KB
        abort(413)
    else: # if JSON, continue
        received_data = request.get_json() # pull the data out of the POST request 

        # now use jsonschema to validate
        validate(received_data, {"maxItems": 1}) # check only one item
        valid_schema_object = { # check that the object is correctly formatted
                "type": "object", # its an object
                "properties": {
                    "data_array": { # called 'data_array'
                        "type" : "array", # that is an array
                        "items": {
                            "type": "array", # consisting of arrays
                            "items": {
                                "type": "number" # which have only numbers inside
                            }
                        }
                    },
                },
                "required": ["data_array"], # 'data_array' is required
                "additionalProperties": False # and nothing else exists in the object
        }
        validate(received_data,valid_schema_object)

        converted_data = received_data['data_array'] # format of the POST comes in as a dict, so just select the array

        # set up psignifit with some standard options
        options = dict();
        options['sigmoidName'] = 'norm';
        options['expType']     = '2AFC';

        options['threshPC']    = 0.7;
        result = ps.psignifit(converted_data,options);

        return jsonify(result['Fit'][0])

if __name__ == "__main__":
	app.run()
