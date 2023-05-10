from flask import Flask, jsonify
from flask_cors import CORS
from comment_analysis import fetch_stock_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/api/stock_recommendations')
def stock_recommendations():
    recommendations = fetch_stock_recommendations()
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run()
