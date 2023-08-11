import json
from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)
HOST = open("db_ip_addr").read().rstrip()
PORT = "5432"

@app.route('/')
def index():
    return json.dumps({'msg': "success"})

@app.route('/all')

def all_users():
    with psycopg2.connect(
    host=HOST,
    port=PORT,  # whatever port postgres is running on
    database="location_db",
    user="postgres",
    password="password") as conn:
        with conn.cursor() as cursor:
            cursor.execute("select * from locations")
            locations = cursor.fetchall()
    conn.close()
    return json.dumps({'locations': locations if locations else "No one's home..."})


app.run(host='0.0.0.0', port=8000, debug=True)
