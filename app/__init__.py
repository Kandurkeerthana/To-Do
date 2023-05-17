"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7gq5269vf5qb5sfkg-a.oregon-postgres.render.com",
        database="todo_cqqc",
        user="root",
        password="Ci0RcmhQ0bihT5poV8j6kldf2bd92OzA")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
