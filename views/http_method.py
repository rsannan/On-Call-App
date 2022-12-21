from flask_smorest import Blueprint
from flask.views import MethodView
from models.http_method import HttpMethodModel
from views.schemas.https_method import HttpMethodReadSchema

blp = Blueprint("http_methods", __name__, 
    url_prefix="/api/http-methods", description="Operations on http methods")


@blp.route("/")
class HttpMethod(MethodView):
    @blp.response(200, HttpMethodReadSchema(many=True))
    def get(self):
        return HttpMethodModel.query.all()