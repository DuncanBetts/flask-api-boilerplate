"""Main module in which we create blueprint and add our routes."""
from flask import Blueprint
from flask_restful import Api
from .resources import UserListResource


blueprint = Blueprint('api', __name__, url_prefix = '/api')
api = Api(blueprint)


api.add_resource(UserListResource, '/user/', endpoint="user")
