#!flask/bin/python
import flask
from flask import make_response, request
from werkzeug.exceptions import HTTPException

app = flask.Flask(__name__)
dictionary = dict()


# @app.route('/')
# def index():
#    return "Hello, World!"


@app.get('/hello')
def print_hello():
    response = make_response('HSE One Love!')
    response.status_code = 200
    response.content_type = 'text/plain'
    return response


@app.errorhandler(HTTPException)
def exception(exp):
    response = make_response()
    response.status_code = 405
    return response


@app.post('/set')
def set_value():
    if request.content_type != 'application/json':
        response = make_response()
        response.status_code = 415
        return response
    else:
        js = request.get_json()
        if 'key' not in js or 'value' not in js:
            response = make_response()
            response.status_code = 400
            return response
    dictionary[js['key']] = js['value']
    response = make_response()
    response.status_code = 200
    return response


@app.get('/get/<string:key>')
def get_value(key):
    if key not in dictionary:
        response = make_response()
        response.status_code = 404
        return response
    else:
        message = {
            "key": key,
            "value": dictionary[key]
        }
        return app.response_class(response=flask.json.dumps(message), status=200, content_type="application/json")


@app.post('/divide')
def div():
    response = make_response()
    response.content_type = 'text/plain'
    if request.content_type != 'application/json':
        response.status_code = 415
        return response
    else:
        js = request.get_json()
        if 'dividend' not in js or 'divider' not in js:
            response.status_code = 400
            return response
        if js['divider'] == 0:
            response.status_code = 400
            return response
        else:
            ans = js['dividend'] / js['divider']
            response.set_data(str(ans))
            response.status_code = 200
            return response


if __name__ == '__main__':
    app.run(debug=True)
