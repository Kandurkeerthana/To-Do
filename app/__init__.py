"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi617u4dadc9vlks590-a.oregon-postgres.render.com",
        database="todo_qnxs",
        user="todo_qnxs_user",
        password="tH03hxtqh9AlNdPYXo14qMuJhvwMIROq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes