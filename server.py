from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import string
import random
import sqlite3
import re

DB_NAME = 'URLS_DB.db'


app = Flask(__name__)
CORS(app)

def connect_to_db():
    
    conn = sqlite3.connect(DB_NAME,timeout=5)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS URLS (
        URL TEXT NOT NULL,
        SHORT_URL TEXT NOT NULL
        )
        ''')
    conn.commit()
    return conn
    

def check_url(original_url):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM URLS WHERE URL =? OR SHORT_URL = ?',(original_url,original_url))
        row = cursor.fetchall()
        if len(row)==0:
            conn.close()
            return create_code(original_url)
        else:
            conn.close()
            return row[0][1]
    except Exception:
        return "Error in connecting to database"
    
def create_code(original_url):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        shortened_url = ''.join(random.choices(string.ascii_letters+string.digits,k=6))
        shortened_url="http://localhost:5000/"+shortened_url
        cursor.execute('SELECT * FROM URLS WHERE URL =?',(original_url,))
        rows = cursor.fetchall()
        #if len(rows)>0:
        #    create_code(original_url)
        cursor.execute('INSERT INTO URLS (URL,SHORT_URL) VALUES(?,?)',(original_url,shortened_url))
        conn.commit()
        conn.close()
        return shortened_url
    except Exception:
        return "Error in connecting to database"

def code_to_url(code):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM URLS WHERE SHORT_URL =?',(code,))
    row = cursor.fetchall()
    conn.commit()
    conn.close()
    if row:
        return row
    else:
        return "Invalid Url"
    


@app.route("/generate",methods=["GET","POST"])
def shorten_url():
    original_url = request.args.get('url')
    if not original_url:
        return jsonify({"message":"Please Enter an URL"}), 200
    if len(original_url)<20:
        return jsonify({"message":"Link too short to be shortened"}), 200
    pattern = r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$'
    match_pattern = re.match(pattern, original_url) is not None
    if match_pattern:
        shorten_url = check_url(original_url)
        return jsonify({"message":shorten_url}), 200
    return jsonify({"message":"invalid URL"}), 200


@app.route("/<code>",methods=["GET","POST"])
def redirect_to_url(code):
    original_url = code_to_url(code)
    if type(original_url) is str:
        return f"<h1>{original_url}</h1>" , 200
    return redirect(original_url[0][0])#,300


if __name__=='__main__':
    app.run(debug=True)
