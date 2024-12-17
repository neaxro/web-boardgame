from data.mysql import BoardgameDB

class BoardgameService():
    def __init__(self, db: BoardgameDB = BoardgameDB()):
        self.db = db
    
    def get_all(self, id, title):
        if id:
            return self.db.get_id(id)
        elif title:
            return self.db.get_title(title)
        else:
            return self.db.get_all()
    
    def get(self, id):
        return self.db.get_id(id)
    
    def insert(self, boardgame_data):
        return self.db.insert(boardgame_data)

    def patch(self, boardgame_data):
        return self.db.update(boardgame_data)

    def delete(self, id):
        return self.db.delete(id)
