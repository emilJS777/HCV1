from flask import make_response, jsonify


# RESPONSE ON SUCCESSFUL CONTROLLER EXECUTION
def response(success, obj, status_code):
    return make_response(jsonify(success=success, obj=obj), status_code)
