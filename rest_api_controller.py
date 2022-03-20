from flask import Flask
from flask_restful import Api, Resource, abort, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dominik_test:dominik@localhost/football'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
import model  # trying to fit to MVC pattern


class Player(Resource):
    @marshal_with(model.serialize_fields)
    def get(self, id):
        result = model.get_player_by_id(id)
        if not result:
            abort(404, message="Couldn't find player with id=" + str(id))
        print(result.last_modified)
        return result, 200

    @marshal_with(model.serialize_fields)
    def post(self, id):
        result = model.get_player_by_id(id)
        if result:
            abort(409, message="Player with id=" + str(id) + " already exists!")
        player = model.create_player(id)
        db.session.add(player)
        db.session.commit()
        return player, 201

    @marshal_with(model.serialize_fields)
    def put(self, id):
        result = model.get_player_by_id(id)
        if not result:
            abort(404, message="Player with id=" + str(id) + " doesn't exist. Cannot update non-existent player.")
        result = model.update_player(result)
        db.session.commit()
        return result, 200

    def delete(self, id):
        result = model.get_player_by_id(id)
        if not result:
            abort(404, message="Player with id=" + str(id) + " doesn't exist. Cannot delete non-existent player.")
        model.delete_player(id)
        db.session.commit()
        return "", 204


class PlayerList(Resource):
    @marshal_with(model.serialize_fields)
    def get(self):
        result = model.get_all_players()
        return result, 200


api.add_resource(Player, "/<int:id>")
api.add_resource(PlayerList, "/all")

if __name__ == '__main__':
    app.run(debug=True)
