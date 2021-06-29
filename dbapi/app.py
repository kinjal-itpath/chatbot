import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

def home():
    query_parameters = request.args
    requirement = query_parameters.get('res')
    mockup = query_parameters.get('mok')
    timeline = query_parameters.get('time')
    budget = query_parameters.get('bud')
    name  = query_parameters.get('nam') 
    email = query_parameters.get('ema') 
    phone  = query_parameters.get('no')
    print(query_parameters)
    # requirement = query_parameters.get('res')
    # published = query_parameters.get('published')
    # author = query_parameters.get('author')
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")
    cursor.execute('''INSERT INTO d3(requirement, mockup, timeline, budget, name, email, phone) VALUES ( ?, ?, ?, ?, ?, ?,?)''', (requirement, mockup,  timeline, budget, name, email, phone))
    print("Table created successfully........")
    conn.commit()
    conn.close()
    return '''<h1>Thank You</h1>'''

if __name__ == "__main__":
    app.run()