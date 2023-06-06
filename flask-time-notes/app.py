from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note(): 
    note = request.json['note']
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    notes.append((timestamp, note))
    return jsonify({'success': True})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)