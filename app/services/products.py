from flask import (
    Blueprint, render_template, jsonify, request
    )
from app.db import client

# Fauna Imports
from faunadb import query as q
from faunadb import errors
from faunadb.objects import Ref

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route("", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        category = request.args.get("category") or None
        if category:
            data = client.query(
                q.map_(
                    lambda x: q.get(x), q.paginate(q.match(
                        q.index("products_by_category"), category)))    
                    )
            response = [i["data"] for i in data["data"]]
            for i in range(0, len(response)):response[i]['id'] = str(data["data"][i]["ref"].id())
            return jsonify(data=response)

        data = client.query(
            q.map_(
                lambda x: q.get(x), q.paginate(q.documents(q.collection("products")))
            )
        )
        response = [i["data"] for i in data["data"]]
        for i in range(0, len(response)):response[i]['id'] = str(data["data"][i]["ref"].id())
        return jsonify(data=response)

    elif request.method == "POST":

        request_data = request.get_json()
        response = client.query(
            q.create(q.collection("products"), {"data": request_data})
        )
        return jsonify(id=response["ref"].id())


@bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def product(id):
    if request.method == "GET":
        try:
            response = client.query(q.get(q.ref(q.collection("products"), id)))
            return jsonify(data=response["data"])

        except errors.NotFound:
            return jsonify(data=None)

    elif request.method == "PUT":
        # update a products document
        try:
            response = client.query(
                q.update(
                    q.ref(q.collection("products"), id), {"data":response.get_json()}
                )
            )
        except Exception as e:
            return jsonify(error=str(e))
    
    elif request.method == "DELETE":
        # delete a reviews document
        try:
            response = client.query(q.delete(q.ref(q.collection("products"), id)))
            return response
        except Exception as e:
            return jsonify(error=str(e))