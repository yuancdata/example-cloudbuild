from flask import Flask, request
import json
import base64
import requests

#Creating a new Flask Web application. It accepts the package name.
app = Flask("Flask_Web_App")
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/generate-data', methods = ['POST']) # set your route (this will be appended to your app URL e.g. your-app.domain/generate-data), and the HTTP method
def opensea_Retreive_Assets():
    envelope = json.loads(request.data.decode('utf-8'))
    payload = json.loads(base64.b64decode(envelope['message']['data'])) # this will allow you to decode the JSON payload if you're accepting a POST request
    
    # Example of reading the JSON `payload`:
    dataset_id = payload['dataset_id']
    table_id = payload['table_id']

    # Example of sending an HTTP request:
    appURL = "https://some-app.domain/request"
    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "dataset_id": dataset_id,
        "table_id": table_id
    }

    jsonBody = json.dumps(body).encode('utf-8') # this will encode your JSON payload for the HTTP POST request
    requests.request("POST", url=appURL, data=jsonBody, headers=headers)
    
    return ('Complete', 200)

# You can create multiple API endpoints for your flask app:
@app.route('/get-data', methods = ['GET']) # set your route (this will be appended to your app URL e.g. your-app.domain/generate-data), and the HTTP method
def opensea_Retreive_Assets():
    # Example of sending an HTTP request:
    appURL = "https://some-app.domain/request"
    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "dataset_id": "some-dataset",
        "table_id": "some-table"
    }

    jsonBody = json.dumps(body).encode('utf-8') # this will encode your JSON payload for the HTTP POST request
    requests.request("POST", url=appURL, data=jsonBody, headers=headers)
    
    return ('Complete', 200)