#!/usr/bin/python3
"""
This module contains the code for the checks endpoing.
"""

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models.check import CheckModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, NoForeignKeysError
from views.schemas.check import CheckCreateSchema, CheckReadSchema, CheckUpdateSchema
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
    def post(self, check_data):
        check = CheckModel()
        check.title = check_data["title"]
        check.url = check_data["url"]
        check.method_id = check_data["method_id"]
        check.status_code = check_data["status_code"]
        check.user_id = check_data["user_id"]

        try:
            db.session.add(check)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while creating a check")

        return check

    @blp.response(200, CheckReadSchema(many=True))
    def get(self):
        checks = CheckModel.query.all()
        return checks


@blp.route("/<string:check_id>")
class Check(MethodView):
    """Defines a check blue print"""
    
    @blp.response(200, CheckReadSchema)
    def get(self, check_id):
        check  = CheckModel.query.get_or_404(check_id)
        return check

    @blp.arguments(CheckUpdateSchema)
    @blp.response(200, CheckUpdateSchema)
    def put(self, check_data, check_id):
        check = CheckModel.query.get_or_404(check_id)
        check.title = check_data["title"]
        check.url = check_data["url"]
        check.method_id = check_data["method_id"]
        check.status_code = check_data["status_code"]
        check.user_id = check_data["user_id"]

        try:
            db.session.add(check)
            db.session.commit()
        except IntegrityError as e:
            abort(500, message=("An error occured while updating a check."
                "The user_id may have no reference to a user"))
        except SQLAlchemyError: 
            abort(500, message="An error occured while updating a check")

        return check

        
    def delete(self, check_id):
        check = CheckModel.query.get_or_404(check_id)

        try:
            db.session.delete(check)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while deleting a check.")

        return {"message": "Check Deleted", "check_id": check.id}