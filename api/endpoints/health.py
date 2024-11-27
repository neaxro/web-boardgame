from flask import request
from flask_restful import Resource

from metrics import time_request, latency_request, count_requests

class Health(Resource):
    def __init__(self):
        pass

    @time_request
    @latency_request
    @count_requests
    def get(self):
        return "Healthy", 200
