from flask_restful import reqparse, fields
from sqlalchemy import func
from rest_api_controller import db


class PlayerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    club = db.Column(db.String(30))
    nationality = db.Column(db.String(30))
    preferred_position = db.Column(db.String(30))
    last_modified = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


player_post_args = reqparse.RequestParser()
player_post_args.add_argument("first_name", type=str, help="Must define player's first name", required=True)
player_post_args.add_argument("last_name", type=str, help="Must define player's last name", required=True)
player_post_args.add_argument("club", type=str)
player_post_args.add_argument("nationality", type=str)
player_post_args.add_argument("preferred_position", type=str)

player_put_args = reqparse.RequestParser()
player_put_args.add_argument("first_name", type=str)
player_put_args.add_argument("last_name", type=str)
player_put_args.add_argument("club", type=str)
player_put_args.add_argument("nationality", type=str)
player_put_args.add_argument("preferred_position", type=str)

serialize_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'club': fields.String,
    'nationality': fields.String,
    'preferred_position': fields.String,
    'last_modified': fields.DateTime(dt_format='iso8601')
}


def get_post_args():
    return player_post_args.parse_args()


def get_put_args():
    return player_put_args.parse_args()


def get_player_by_id(id):
    return PlayerModel.query.filter_by(id=id).first()


def create_player(id):
    args = get_post_args()
    return PlayerModel(id=id, first_name=args['first_name'], last_name=args['last_name'], club=args['club'],
                       nationality=args['nationality'], preferred_position=args['preferred_position'])


def update_player(player):
    args = get_put_args()

    # TODO maybe reduce with exec
    if args['first_name']:
        player.first_name = args['first_name']
    if args['last_name']:
        player.last_name = args['last_name']
    if args['club']:
        player.club = args['club']
    if args['nationality']:
        player.nationality = args['nationality']
    if args['preferred_position']:
        player.preferred_position = args['preferred_position']
    return player


def delete_player(id):
    PlayerModel.query.filter_by(id=id).delete()


def get_all_players():
    return PlayerModel.query.order_by(PlayerModel.id).all()
