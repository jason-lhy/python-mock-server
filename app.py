import json
import os
import uuid
import sqlalchemy as db
import pymysql
from flask import Flask, jsonify, request
from model.expectation import Expectation
from query_helper import dict_to_query

MYSQL_USER = os.environ["DB_USER"]
MYSQL_PW = os.environ["DB_PW"]
MYSQL_DB_NAME = os.environ["DB_NAME"]
MYSQL_HOST = os.environ.get("DB_HOST", "127.0.0.1")
MYSQL_PORT = os.environ.get("DB_PORT", "3306")

pymysql.install_as_MySQLdb()
engine = db.create_engine(
    f"mysql://{MYSQL_USER}:{MYSQL_PW}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}")
connection = engine.connect()
app = Flask(__name__)


@app.route('/expectation', methods=["POST", "GET"])
def set_expectation():
    if request.method == "GET":
        return "Get Request"
    elif request.method == "POST":
        item_id = str(uuid.uuid4())
        expectation = Expectation(
            path=request.json['path'],
            method=request.json['method'],
            arguments={
                k: str(v) for k, v in request.json['arguments'].items()},
            response=request.json['response']
        )
        query = f"""
        INSERT INTO 
            expectations (id, path, method, arguments, response)
        VALUES (
            '{item_id}', '{expectation.path}', '{expectation.method}', '{json.dumps(expectation.arguments)}', '{json.dumps(expectation.response)}');"""
        db.text(query)
        connection.execute(query)
        return jsonify(expectation.__dict__)
    return 'hello world'


@app.route('/<path:u_path>', methods=["POST", "GET", "PUT", "PATCH", "DELETE"])
def hello_world(u_path):
    if request.method == 'GET':
        args = request.args.to_dict()
    else:
        args = request.json
    query = f"""
    SELECT * FROM expectations WHERE path = '/{u_path}' AND method = '{request.method}' {dict_to_query(args)}
    """
    res_json = json.loads(
        dict(connection.execute(query).fetchone())['response'])
    return jsonify(res_json)
