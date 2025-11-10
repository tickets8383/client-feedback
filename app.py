from flask import Flask, request, jsonify, render_template
import sqlite3
import re
from datetime import datetime

app = Flask(__name__)
DB_NAME = 'insights.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            feedback_text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    if not data or 'customer_name' not in data or 'feedback_text' not in data:
        return jsonify({"error": "Missing data"}), 400

    customer_name = data['customer_name']
    feedback_text = data['feedback_text']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO feedback (customer_name, feedback_text) VALUES (?, ?)',
        (customer_name, feedback_text)
    )
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "message": "Feedback added"}), 201

@app.route('/api/feedback', methods=['GET'])
def get_all_feedback():
    conn = get_db_connection()
    feedback = conn.execute('SELECT * FROM feedback ORDER BY timestamp DESC').fetchall()
    conn.close()
    return jsonify([dict(row) for row in feedback])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
