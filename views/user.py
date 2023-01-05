from flask.views import MethodView
from flask_smorest import Blueprint, abort
from views.schemas.user import  CreateUserSchema, ReadUserSchema, UserUpdateSchema, UserLoginSchema
from models.user import UserModel
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256
from db import db


blp = Blueprint("user", __name__, url_prefix="/api/users", description="Operations on users")

@blp.route("/")
class UserList(MethodView):
    @blp.arguments(CreateUserSchema)
    @blp.response(201, CreateUserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        user.password = pbkdf2_sha256.hash(user_data["password"])
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User with the given email already exists.")
        except SQLAlchemyError:
            abort(400, message="User with the given email already exists.")

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

    # def delete(self, user_id):
    #     user = UserModel.query.get_or_404(user_id)
        
    #     return {"message": "User deleted", "user_id": user.id}, 200



@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.email == user_data["email"]).first()
        
        if not user:
            abort(400, message="Invalid email or password.")
        elif not pbkdf2_sha256.verify(user_data["password"], user.password):
            abort(400, message="Invalid email or password.")

        token = create_access_token(identity=user.id)
        
        return {"access_token": token}
        
        