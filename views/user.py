from flask.views import MethodView
from flask_smorest import Blueprint, abort
from views.schemas.user import PlainUserSchema
from models.user import UserModel
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from db import db


blp = Blueprint("user", __name__, url_prefix="/users", description="Operations on users")

@blp.route("/")
class User(MethodView):
    @blp.arguments(PlainUserSchema)
    @blp.response(201, PlainUserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User with the given email already exists")
        except SQLAlchemyError:
            abort(400, message="User with the given email already exists")

        return user

    
    