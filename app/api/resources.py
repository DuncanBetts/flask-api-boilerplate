"""This is main module where we should define all resources."""
from flask import jsonify
from flask_restful import Resource


class BaseResource(Resource):
    """This is a base class for any resource."""


class UserListResource(BaseResource):
    """User list"""

    def get(self):
        """Get method for UserListResource"""
        return jsonify({ 'username': 'marek' })