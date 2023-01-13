#!/usr/bin/python3
"""
This module contains the code for the checks endpoing.
"""

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models.check import CheckModel
from models.http_header import HTTPHeaderModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from views.schemas.check import CheckCreateSchema, CheckReadSchema, CheckUpdateSchema
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from db import db


blp = Blueprint("check", __name__,
    url_prefix="/api/checks", description="Operations on checks")
    
@blp.route("/")
class CheckList(MethodView):
    """
    Defines a class for dealing with api responses that may include
    a list of checks on the /api/checks endpoint
    """
    @blp.arguments(CheckCreateSchema)
    @blp.response(200, CheckCreateSchema)
    @jwt_required()
    def post(self, check_data):
        user_id = get_jwt_identity();
        check = CheckModel()
        check.title = check_data["title"]
        check.url = check_data["url"]
        check.method_id = check_data["method_id"]
        check.status_code = check_data["status_code"]
        check.user_id = user_id
        check.headers = [HTTPHeaderModel(**h) for h in check_data.get("headers")]
        check.data = check_data.get("data")

        try:
            db.session.add(check)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while creating a check")

        return check

    @blp.response(200, CheckReadSchema(many=True))
    @jwt_required()
    def get(self):
        checks = CheckModel.query.filter(CheckModel.user_id == get_jwt_identity()).all()
        return checks


@blp.route("/<string:check_id>")
class Check(MethodView):
    """Defines a check blueprint"""
    
    @blp.response(200, CheckReadSchema)
    @jwt_required()
    def get(self, check_id):
        check  = CheckModel.query.get_or_404(check_id)
        user_id = get_jwt_identity()
        if check.user_id != user_id:
            abort(401, message="Looks like this check belongs to another user.")
        return check

    @blp.arguments(CheckUpdateSchema)
    @blp.response(200, CheckUpdateSchema)
    @jwt_required()
    def put(self, check_data, check_id):
        check = CheckModel.query.get_or_404(check_id)
        if check.user_id != get_jwt_identity():
            abort(400, message="Looks like this check belongs to another user.")
            
        check.title = check_data["title"]
        check.url = check_data["url"]
        check.method_id = check_data["method_id"]
        check.status_code = check_data["status_code"]
        # check.headers = [HTTPHeaderModel(**h) for h in check_data["headers"]]

        # abort(503, message="This feature is currently undergoing some maintenance.")

        try:
            db.session.add(check)
            db.session.commit()
        except IntegrityError as e:
            print(e)
            abort(500, message=("An error occured while updating a check."
                "The user_id may have no reference to a user"))
        except SQLAlchemyError as e:
            print(e)
            abort(500, message="An error occured while updating a check")

        return check

    @jwt_required()
    def delete(self, check_id):
        check = CheckModel.query.get_or_404(check_id)

        if check.user_id != get_jwt_identity():
            abort(401, message="Looks like this check belongs to another user.")

        try:
            db.session.delete(check, )
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while deleting a check.")

        return {"message": "Check Deleted", "check_id": check.id}