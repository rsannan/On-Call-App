from flask.views import MethodView
from flask_smorest import Blueprint, abort
from views.schemas.user import  CreateUserSchema, ReadUserSchema, UserUpdateSchema
from models.user import UserModel
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from db import db


blp = Blueprint("user", __name__, url_prefix="/api/users", description="Operations on users")

@blp.route("/")
class UserList(MethodView):
    """
    Defines a UserList class that deals with
    payloads which include a list of data
    """
    @blp.arguments(CreateUserSchema)
    @blp.response(201, CreateUserSchema)
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

    
    @blp.response(201, ReadUserSchema(many=True))
    def get(self):
        users = UserModel.query.all()
        return users
        

@blp.route("/<string:user_id>")
class User(MethodView):
    @blp.response(200, ReadUserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user


    @blp.arguments(UserUpdateSchema)
    @blp.response(201, UserUpdateSchema)
    def put(self, user_data, user_id):
        user = UserModel.query.get_or_404(user_id)
        user.firstname = user_data["firstname"]
        user.lastname = user_data["lastname"]
        user.phone = user_data["phone"]

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while updating a user.")

        return user

        