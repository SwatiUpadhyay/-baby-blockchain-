# app.py

from flask import Flask, render_template, request, redirect, url_for
from blockchain.chain import Blockchain
from datetime import datetime  # 🌟 New import for pretty timestamps

app = Flask(__name__)
blockchain = Blockchain()

# 💫 Custom Jinja filter to convert UNIX time to readable time
@app.template_filter('format_datetime')
def format_datetime(value):
    return datetime.fromtimestamp(value).strftime('%d-%b-%Y %I:%M %p')

@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain)

@app.route('/add', methods=['POST'])
def add_block():
    data = request.form['data']
    blockchain.add_block(data)
    return redirect(url_for('index'))

@app.route('/validate')
def validate():
    is_valid = blockchain.is_chain_valid()
    return f"Chain is valid? {is_valid}"

if __name__ == '__main__':
    app.run(debug=True)
