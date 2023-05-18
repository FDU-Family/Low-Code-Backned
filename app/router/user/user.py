from flask import Blueprint, jsonify, request
from app import db

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/get")
def get():
    return jsonify({"info": "获取成功"})

