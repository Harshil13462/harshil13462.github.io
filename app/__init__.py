# __init__.py
from flask import Flask, request, jsonify, render_template
from app.utils.pokerMC import calculate_odds

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poker')
def poker():
    return render_template('poker.html')

@app.route('/hexGame')
def hex_game():
    return render_template('hexGame.html')


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    try:
        data = request.get_json(force=True)
        hand = data.get('hand')
        board = data.get('board', [])

        if not hand or len(hand) != 2:
            return jsonify({"error": "Invalid hand input"}), 400

        odds = calculate_odds(hand, board)
        return jsonify(odds)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
