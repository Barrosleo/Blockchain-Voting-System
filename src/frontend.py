from flask import Flask, render_template, request
from backend import vote

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def cast_vote():
    candidate_id = request.form['candidate_id']
    voter_private_key = request.form['voter_private_key']
    tx_hash = vote(candidate_id, voter_private_key)
    return f"Vote cast successfully! Transaction hash: {tx_hash}"

if __name__ == "__main__":
    app.run(debug=True)
