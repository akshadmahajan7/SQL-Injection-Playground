import sqlite3
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    # Reset table for fresh demo
    c.execute('DELETE FROM users') 
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSecretPass123')")
    c.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest123')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

# --- VULNERABLE ENDPOINT ---
@app.route('/vulnerable', methods=['POST'])
def vulnerable_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # FLAW: Direct string concatenation creates the vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    response = {"query": query, "success": False, "message": "Invalid Credentials", "user": None}
    
    try:
        c.execute(query)
        user = c.fetchone()
        if user:
            response["success"] = True
            response["message"] = f"Login Successful!"
            response["user"] = user[1]
    except Exception as e:
        response["message"] = f"SQL Syntax Error: {str(e)}"
    
    conn.close()
    return jsonify(response)

# --- SECURE ENDPOINT ---
@app.route('/secure', methods=['POST'])
def secure_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # FIX: Parameterized queries treat input as data, not code
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    display_query = f"SELECT * FROM users WHERE username = ? AND password = ? (Params: {username}, {password})"
    
    response = {"query": display_query, "success": False, "message": "Invalid Credentials", "user": None}

    try:
        c.execute(query, (username, password))
        user = c.fetchone()
        if user:
            response["success"] = True
            response["message"] = f"Login Successful!"
            response["user"] = user[1]
    except Exception as e:
        response["message"] = f"Error: {str(e)}"

    conn.close()
    return jsonify(response)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
