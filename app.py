from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory alerts list (resets every time server restarts)
alerts = [
    {"id": 1, "text": "Suspicious post related to cocaine", "risk_score": "High"},
    {"id": 2, "text": "Wallet W1 flagged for suspicious transactions", "risk_score": "Medium"},
]

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts)

@app.route('/alert/<int:alert_id>/investigate', methods=['POST'])
def mark_alert_investigated(alert_id):
    global alerts
    alerts = [alert for alert in alerts if alert["id"] != alert_id]
    return jsonify({"message": f"Alert {alert_id} marked as investigated"}), 200

@app.route('/graph', methods=['GET'])
def get_graph():
    graph_data = {
        "nodes": [
            {"id": "BuyerA", "group": "buyer"},
            {"id": "SellerX", "group": "seller"},
            {"id": "Wallet1", "group": "wallet"}
        ],
        "links": [
            {"source": "BuyerA", "target": "SellerX"},
            {"source": "SellerX", "target": "Wallet1"}
        ]
    }
    return jsonify(graph_data)

if __name__ == '__main__':
    app.run(debug=True)
