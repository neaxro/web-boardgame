from flask import jsonify, request
from flask_restful import Resource

from services.boardgame import BoardgameService
from metrics import count_requests, time_request, latency_request

class Boardgame(Resource):
    def __init__(self):
        self.bs = BoardgameService()
    
    @count_requests
    @time_request
    @latency_request
    def get(self):
        try:
            query_id = request.args.get("id")
            query_title = request.args.get("title")

            return self.bs.get_all(query_id, query_title), 200

        except Exception as e:
            return {"error": "Something went wrong", "details": str(e)}, 500

    @count_requests
    @time_request
    @latency_request
    def post(self):
        try:
            boardgame_data = request.get_json()

            try:
                boardgame_id = self.bs.insert(boardgame_data)
                return {"message": "Boardgame created successfully", "boardgame_id": boardgame_id}, 201
            except Exception as e:
                return {"message": "Failed to create boardgame", "details": str(e)}, 500

        except Exception as e:
            return {"error": "Something went wrong", "details": str(e)}, 500
